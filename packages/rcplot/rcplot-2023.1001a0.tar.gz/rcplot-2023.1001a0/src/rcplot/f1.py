import plotly.express as px

from .utils import pred2f1


def calculate_metrics(df, label_df):
    # calculate f1 scores
    results = pred2f1(df)

    # map class labels
    desc_mapping = dict(zip(label_df["id"], label_df["description"]))
    grp_mapping = dict(zip(label_df["id"], label_df["group_code"]))
    desc_mapping.update({"OVERALL": "OVERALL"})
    grp_mapping.update({"OVERALL": "OVERALL"})

    results["Class_description"] = results["Class"].map(desc_mapping)
    results["Functional_group"] = results["Class"].map(grp_mapping)
    return results[["Class_description", "Functional_group", "F1_score"]]

def plotf1(df, label_df):
    results=calculate_metrics(df, label_df)
    fig = px.bar(results,
                 y="Class_description",
                 x="F1_score",
                 color="Functional_group",
                 facet_row="Functional_group"
                 )

    fig.update_yaxes(matches=None, showticklabels=True)

    fig.update_layout(height=900, width=900,
                      yaxis=dict(title=""),
                      xaxis=dict(title="F1 Score"))

    fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
    fig.for_each_yaxis(lambda y: y.update(title=""))

    # fig.write_html("../data/F1_scores.html")
    fig.show()