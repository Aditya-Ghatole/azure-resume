Cloud Resume Challenge (Azure Edition)

This repository documents the implementation of the Cloud Resume Challenge using Microsoft Azure services. The objective is to design, build, and deploy a resilient, production-grade resume website that showcases cloud platform expertise, automation, and modern DevOps practices.

Overview

The Cloud Resume Challenge (Azure Edition) demonstrates proficiency in deploying a static resume website on Azure, integrating a serverless backend for visitor tracking, and utilizing continuous integration and deployment pipelines. This solution highlights the advantages of cloud-native design and the operational benefits of automation.
Solution Architecture

High-level components:

    Frontend: Static website hosted on Azure Storage (HTML, CSS, JavaScript)

    Backend: Python-based RESTful API implemented with Azure Functions

    Database: Azure Table Storage for persisting visitor statistics

    Authentication: Optional integration with Azure Active Directory or anonymous access

    Infrastructure as Code: Resource provisioning managed via ARM/Bicep or Terraform scripts

    CI/CD Pipeline: Automated build and deployment with GitHub Actions or Azure DevOps Pipelines

