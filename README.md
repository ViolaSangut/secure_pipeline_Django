# 🔐 Secure CI/CD Pipeline Setup & Execution – Django App

## 📁 Repository

**GitHub Repo:** [secure\_pipeline\_Django](https://github.com/ViolaSangut/secure_pipeline_Django.git)

---

## 🚀 Overview

This pipeline demonstrates a complete DevSecOps workflow using:

- **GitHub Actions** (CI/CD automation)
- **SonarCloud + CodeQL** (Static Analysis)
- **Trivy + GitLeaks** (Dependency & Secrets Scanning)
- **OWASP ZAP** (Dynamic Testing)
- **DockerHub + EC2** (Deployment)

Each stage is automated and produces reports visible in GitHub or third-party dashboards.

---

## ⚙️ 1. CI/CD Workflow

### GitHub Actions Setup

The workflow is defined in `.github/workflows/pipeline.yml`.

Steps include:

- Build Docker image
- Run static scans
- Detect secrets and vulnerabilities
- Push Docker image to DockerHub
- SSH into EC2 and deploy the container

### Prerequisites

- GitHub repository connected to SonarCloud and CodeQL
- DockerHub account + Personal Access Token (PAT)
- Running EC2 instance with Docker installed
- GitHub secrets configured:
  - `DOCKER_USERNAME`, `DOCKER_PASSWORD`
  - `EC2_HOST`, `EC2_USER`, `EC2_KEY`
  - `DAST_TARGET_URL`

---

## 🔍 2. Static Application Security Testing (SAST)

### Tools: SonarCloud + CodeQL

**SonarCloud:**

- Detects bugs, vulnerabilities, and code smells.
- Reports available on [SonarCloud Dashboard](https://sonarcloud.io/).

**CodeQL:**

- GitHub-native code analysis.
- Results are available under **Security > Code scanning alerts** in the repo.

---

## 🔐 3. Secrets & Dependency Scanning

### Tools: Trivy + GitLeaks

**Trivy:**

- Scans `requirements.txt` for vulnerable packages.

**GitLeaks:**

- Detects hardcoded secrets like tokens and credentials.

**Reports:**

- Outputs shown in GitHub Actions logs.

---

## 🐳 4. Container Image Security

### Tool: Trivy (Image Scan)

- Trivy scans the Docker image after it's built.
- Detects OS and application layer vulnerabilities.

**DockerHub:**

- Image is only pushed if scan passes.
- Check tags and history on DockerHub after a successful push.

---

## ☁️ 5. Deployment to EC2

Once image is pushed:

- GitHub Actions SSHs into the EC2 instance.
- Pulls the image and runs the container.

### Deployment Steps

1. Ensure Docker is installed on EC2.
2. Open necessary ports (e.g., 8000).
3. Add a public IP or domain name.

Example:

```bash
ssh -i "your-key.pem" ec2-user@your-ec2-ip

docker pull yourdockerusername/yourimagename:tag
docker run -d -p 8000:8000 yourdockerusername/yourimagename:tag
```

Access the app at: `http://<your-ec2-ip>:8000/`

---

## 🌐 6. Dynamic Application Security Testing (DAST)

### Tool: OWASP ZAP

- Runs in GitHub Actions after the app is live on EC2.
- Target URL is defined by the GitHub Secret `DAST_TARGET_URL`.
- ZAP simulates attacks such as XSS and SQLi.

### Reports:

- Summary output in GitHub Actions logs.
- Can be configured to save JSON or HTML reports as artifacts.

---

## 📌 Summary Pipeline Flow

1. Code pushed to GitHub.
2. SonarCloud, CodeQL, GitLeaks, Trivy scans run.
3. Docker image built, scanned, and pushed to DockerHub.
4. GitHub Actions connects to EC2 and deploys the app.
5. OWASP ZAP performs DAST using the live URL.

---

## 📂 Example Secrets Configuration

- `DOCKER_USERNAME`: DockerHub username
- `DOCKER_PASSWORD`: DockerHub PAT
- `EC2_HOST`: EC2 public IP
- `EC2_USER`: usually `ec2-user` or `ubuntu`
- `EC2_KEY`: contents of your `.pem` SSH key
- `DAST_TARGET_URL`: public URL of the running app

---

Feel free to fork the repo, configure your secrets, and try the pipeline!
