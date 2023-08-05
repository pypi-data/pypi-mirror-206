import plotly.graph_objects as go
import plotly.express as px

from .utils import error_per_image

def cover_error(df, label_df):
    ce = error_per_image(df, 'human_classification', 'model_classification', 'image_id')

    # map class labels
    desc_mapping = dict(zip(label_df["id"], label_df["description"]))
    grp_mapping = dict(zip(label_df["id"], label_df["group_code"]))

    ce["Class_description"] = ce.human_classification.map(desc_mapping)
    ce["Functional_group"] = ce.human_classification.map(grp_mapping)

    return ce[["image_id", "cover_error", "Class_description", "Functional_group"]]

def plotcover(datadf, label_df):
    df = cover_error(datadf, label_df)

    df_in = df.sort_values("Functional_group")

    fig = go.Figure()

    clrs = dict(zip(df.Functional_group.unique(), px.colors.qualitative.Plotly[:len(df.Functional_group.unique())]))

    for cl in df_in.Class_description.unique():
        df_c = df_in[df_in.Class_description == cl]
        group = df_c.Functional_group.unique()[0]

        fig.add_trace(go.Box(
            x=df_c.cover_error,
            y0=cl,
            name=group,
            legendgroup=group,
            line=dict(color=clrs[group])
        ))
    fig.update_layout(
        xaxis_title="Error in Image Cover Estimate"
    )

    names = set()
    fig.for_each_trace(
        lambda trace:
        trace.update(showlegend=False)
        if (trace.name in names) else names.add(trace.name))

    fig.update_layout(
        yaxis=dict(autorange="reversed"),
        width=900,
        height=800)

    fig.show()
