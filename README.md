# 🔐 Secure CI/CD Pipeline Setup & Execution – Django App

## 📁 Repository

**GitHub Repo:** [secure\_pipeline\_Django](https://github.com/ViolaSangut/secure_pipeline_Django.git)

---

### Prerequisites

- GitHub repository connected to SonarCloud and CodeQL. Follow the following link on how to connect sonarcloud with  github https://www.sonarsource.com/learn/integrating-sonarcloud-with-github/
- DockerHub account + Personal Access Token (PAT). set duckerhub token in your githb secrets.
- Running EC2 instance with Docker installed
- GitHub secrets configured:
  - `DOCKER_USERNAME`, `DOCKER_PASSWORD`
  - `SONAR_PROJECT_KEY`, `SONAR_ORG`, `SONAR_TOKEN`
  - `DAST_TARGET_URL` 

---

## 🚀 Overview

This pipeline demonstrates a complete DevSecOps workflow using:


- **GitHub Actions** (CI/CD automation)
- **SonarCloud + CodeQL** (Static Analysis)
- **Dependabot** (SCA)
- **Trivy** (Image & Secrets Scanning)
- **OWASP ZAP** (Dynamic Testing)
- **DockerHub + EC2** (Deployment)

Each stage is automated and produces reports visible in GitHub or third-party dashboards.

---

## ⚙️ 1. CI/CD Workflow

### GitHub Actions Setup

The  CI workflow is defined in `.github/workflows/docker_ci.yml`.
The file Automates the following steps

- Build Docker image
- Push Docker image to DockerHub

Note:
Manual step
- SSH into EC2 or your deployment environment and deploy the container

The inegrated tools also runs the following tests automatically everytime code is committed.
- Run SCA, SAST and DAST scans
- Scans Image and Detect secrets 

Manual step

- SSH into EC2 or your deployment environment and deploy the container


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

### Tools: Trivy 

**Trivy:**

- Scans `requirements.txt` for vulnerable packages.

**Reports:**

- Outputs shown in GitHub Actions logs.

---

## 🐳 4. Container Image Security

### Tool: Trivy (Image Scan)

- Trivy scans the Docker image after it's built.
- Detects OS and application layer vulnerabilities.

**DockerHub:**

- Check tags and history on DockerHub after a successful push.

---

## ☁️ 5. Deployment to EC2

Once image is pushed:

-  SSHs into the EC2 instance.
- Pull the image and run the container.

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
4. OWASP ZAP performs DAST using the live URL.

---

## 📌 how to improve
- Image is only pushed if scan passes.
- Automate deployment to server is scans passes.
Feel free to fork the repo, configure your secrets, and try the pipeline!
