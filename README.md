# AWS Cost Anomaly Finder (with AI Explanations)

## 📌 Project Overview

The **AWS Cost Anomaly Finder** is a cloud-native FinOps project designed to automatically detect unusual daily AWS spending and generate human-readable explanations for cost spikes.

The system combines **deterministic anomaly detection** (math-based baselines and thresholds) with an **optional AI explanation layer**, ensuring accuracy, cost control, and production-grade reliability.

This project was intentionally built to be:

- Low-cost (safe for personal AWS accounts)
- Infrastructure-as-Code driven
- Resume and interview ready

---

## 🏗️ Architecture Overview

**Core AWS Services Used**:

- **AWS Lambda** – Cost analysis and anomaly detection
- **AWS Cost Explorer API** – Daily cost data source
- **Amazon DynamoDB** – Historical cost storage
- **Amazon SNS** (optional, future step) – Alerting
- **Terraform** – Infrastructure provisioning

**High-Level Flow**:

1. Lambda pulls daily cost data from Cost Explorer
2. Cost data is stored in DynamoDB
3. Historical costs are used to calculate a baseline
4. Current cost is compared against the baseline
5. If anomalous, AI generates an explanation (optional)

---

## 🧠 Anomaly Detection Design

### Baseline Calculation

- Uses the average cost of the previous **N days** (default: 7)
- The current day is **explicitly excluded** to avoid self-normalization

### Anomaly Rule

```text
Current Cost > (Baseline × Anomaly Multiplier)
```

- Default multiplier: **1.5**
- Fully configurable via environment variables

### Cold-Start Handling

- When insufficient historical data exists, anomaly detection is skipped
- Prevents false positives during early deployment

---

## 🤖 AI Explanation Layer (Optional)

AI is **not** used for detection.
Instead, it is applied **only after** a deterministic anomaly is identified.

### Why This Design?

- Prevents false positives
- Keeps AI usage costs near zero
- Improves explainability instead of decision-making

### Example AI Output

- Plain-English summary of the anomaly
- Top cost-driving services
- Practical optimization recommendations

AI usage is controlled via a feature flag:

```text
AI_ENABLED = true | false
```

---

## ⚙️ Configuration

All behavior is controlled using Lambda environment variables:

| Variable           | Description            | Default |
| ------------------ | ---------------------- | ------- |
| MODE               | test or prod           | test    |
| DAYS_BACK          | Cost Explorer lookback | 7       |
| BASELINE_DAYS      | Days used for baseline | 7       |
| ANOMALY_MULTIPLIER | Sensitivity threshold  | 1.5     |
| AI_ENABLED         | Enable AI explanations | false   |

---

## 🧪 Testing Strategy

To avoid unnecessary AWS spend:

- Test mode injects artificial cost spikes
- No scheduled execution required
- Manual Lambda invocation used for validation

This ensures the project is:

- Safe for personal AWS accounts
- Fully testable without continuous usage

---

## 🛠️ Infrastructure as Code

All resources are provisioned using **Terraform**:

- Lambda function
- IAM roles and policies
- DynamoDB table
- Environment variables

This allows:

- Repeatable deployments
- Clean teardown
- Version-controlled infrastructure

---

## 🔐 Security & Best Practices

- No hardcoded credentials
- IAM follows least-privilege principles
- Environment-based configuration
- Defensive error handling

---

## 📈 Future Enhancements

- SNS or email alerting
- Weekly cost summaries
- Cost visualization with Athena + QuickSight
- Replace mock AI with Amazon Bedrock

---

## 💼 Why This Project Matters

This project demonstrates real-world cloud engineering skills:

- FinOps awareness
- Deterministic system design
- Cost-efficient AI usage
- AWS service integration
- Production-minded decision making

It reflects how cost monitoring systems are built in professional cloud environments.

---

## 📎 Tech Stack

- AWS Lambda (Python)
- AWS Cost Explorer
- DynamoDB
- Terraform
- Optional AI layer (mock / extensible)

---

**Author**: Sreekuttan Chandran Latha
