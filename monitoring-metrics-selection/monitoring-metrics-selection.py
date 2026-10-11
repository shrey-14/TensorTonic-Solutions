def compute_monitoring_metrics(system_type: str, y_true: list, y_pred: list) -> dict:
    """
    Returns a dictionary of metrics.
    """
    # Write code here
    if system_type == "classification":
        tp, tn, fp, fn = 0, 0, 0, 0
        for i, j in zip(y_true, y_pred):
            if i == j == 1:
                tp += 1
            elif i == j == 0:
                tn += 1
            elif i == 1 and j == 0:
                fp += 1
            elif i == 0 and j == 1:
                fn += 1

        accuracy = (tp + tn) / len(y_true)
        precision = 0.0 if (tp + fp) == 0 else (tp / (tp + fp))
        recall = 0.0 if (tp + fn) == 0 else (tp / (tp + fn))
        f1 = 0.0 if (precision + recall) == 0 else ((2 * precision * recall) / (precision + recall))

        return {"accuracy": accuracy, "precision": precision, "recall": recall, "f1": f1}
        
    elif system_type == "regression":
        mae = (1 / len(y_true)) * sum([abs(yt - yp) for yt, yp in zip(y_true, y_pred)])
        rmse = ((1 / len(y_true)) * sum([(yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)])) ** (1/2)

        return {"mae": mae, "rmse": rmse}

    elif system_type == "ranking":
        top_3_scores = sorted(y_pred, reverse=True)[:3]
        top_3_relevance = [0, 1, 2]

        total_relevant = [i for i in range(len(y_true)) if y_true[i] == 1]

        pk = len(set(top_3_relevance).intersection(set(total_relevant))) / 3
        rk = 0.0 if len(total_relevant) == 0 else len(set(top_3_relevance).intersection(set(total_relevant))) / len(total_relevant)

        return {"precision_at_3": pk, "recall_at_3": rk}
        