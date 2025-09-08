Cloud Resume Challenge (Azure Edition)

This repository documents the implementation of the Cloud Resume Challenge using Microsoft Azure services. The objective is to design, build, and deploy a resilient, production-grade resume website that showcases cloud platform expertise, automation, and modern DevOps practices.

Overview

The Cloud Resume Challenge (Azure Edition) demonstrates proficiency in deploying a static resume website on Azure, integrating a serverless backend for visitor tracking, and utilizing continuous integration and deployment pipelines. This solution highlights the advantages of cloud-native design and the operational benefits of automation.
Solution Architecture

High-level components:

    Frontend: Static website hosted on Azure Storage (HTML, CSS, JavaScript)

    Backend: Python-based RESTful API implemented with Azure Functions

    Database: Azure Cosmos DB for persisting visitor statistics

    Infrastructure as Code: Resource provisioning managed via ARM/Bicep or Terraform scripts

    CI/CD Pipeline: Automated build and deployment with GitHub Actions or Azure DevOps Pipelines


## Credits

This project’s front-end design is based on the **Luther template** by [Styleshout](https://www.styleshout.com/).  
The template is licensed under the [Creative Commons Attribution 3.0 License](https://creativecommons.org/licenses/by/3.0/).

The template has been customized and adapted for this project.
