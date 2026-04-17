---
layout: default
title: "BSc/MSc Thesis Subjects | Asterios Katsifodimos"
---

<br/>

#### Bachelor and Master thesis subject ideas

I like to advise theses whose results can be relevant to real-life problems. Some of the thesis subjects below might include an internship oportunity with companies like KPMG in Amsterdam, SAP Innovation Center in Berlin, KTH in Stockholm, TU Berlin, or the - under development -  Delft Data Science Platform. I like to define thesis subjects in a high-level fashion so that students can steer the subject to their liking (more on systems, or theory), level (Bachelor or Master), and skill-set. If you are interested in any of the subjects below, or want to propose one that would match my style of research, please get in contact with me! 

##### Big Data Analytics &amp; Stream Processing
###### Bridging Linear and Relational Algebra for Scalable Data Science

Linear algebra operations are at the core of many Machine Learning (ML) pipelines. At the same time, a considerable amount of the effort for solving data analytics problems is spent in data preparation. As a result, end-to-end ML pipelines often consist of (i) relational operators used for joining the input data, (ii) user defined functions used for feature extraction and vectorization, and (iii) linear algebra operators used for model training and crossvalidation. Often, these pipelines need to scale out to large datasets. In this case, these pipelines are usually implemented on top of dataflow engines like Hadoop, Spark, or Flink. These dataflow engines implement relational operators on row-partitioned datasets. However, efficient linear algebra operators use block-partitioned matrices.

The goal of this thesis would be to optimize Data Science pipelines by applying ideas from database optimizers in large Big Data pipelines which indlude both linear and relational algebra operations. The thesis can take over work on the theory side (how can we represent "query plans" so that we can optimize them?) and/or on the practical side (how can be design novel physical operators to use in scalable ML pipelines?).

###### Executing Transactions in Modern Stream Processors
Stream processors such as Apache Flink, Storm or APEX are emerging in the industry as a tool to perform both analytical workloads (e.g., monitoring log files, sensors, and micro-services) but also mission critical services such as fraud detection in credit-card transactions. Modern streaming systems are now on an arms-race to provide first-class support for application state with strong state consistency guarantees in the presence of failures. 

At the same time, there is growing need for executing high-throughput transaction directly on the stream processor, rather than on a traditional database system. The goal of this thesis is to investigate ways of executing transactions on the application state of modern stream processing systems (e.g., Apache Flink). 

###### Dataset Versioning For Social Data Science
Version control is a very important part of every development process. Developers typically branch from a version of a software system, apply their own changes and then merge their changes to a master branch. Various tools and systems exist, the most famous and successful being Git (and the gitHub website). Git, however, is designed for the develpment process of software, not data. This thesis should create tools and a platform, very similar to the ideas behind Github, but for very large datasets. There are a lot of challenges associated with dataset versioning. Most of them stem from the sheer volume of datasets which can be in the order of Terabytes. It is evident that retrieving, comparing (and creating deltas) and storing data of such a volume is a non-trivial task. This thesis will investigate current techniques for version management of massive datasets, and propose changes to those techniques, in order to tackle the challenges mentioned above. 

###### Data Lakes
The aim of this thesis work is to understand the state of the art in technology for data lakes. More specifically, the student will work on implementing novel data processing functionality and
services into an existing data-lake platform.

##### Scalable Machine Learning 

###### Scalable Inference with Deep-Learning Models in the GPU Clouds 
Nowadays we witness the proliferation of solutions for scalable Machine LEarning Inference (e.g., Google Cloud Machine Learning, SAP Leonardo ML foundations, Amazon's AI on AWS). In these platforms, a specialized model is first trained and then used to respond to users' requests, such as image recognition, where the user sends an image to a running service and receives a set of objects that are found in that image. Tensorflow and the Inception deep-learning model are typical examples of technologies used for such ML inference. However, such inference is very slow on CPUs and cloud companies typically use GPUs to perform inference at scale. In Software-as-a-Service (SaaS) offerings, the objective of a service provider is to allocate and de-allocate resources (CPU, GPU, memory and network) to satisfy its SLAs, while minimizing its operational costs. Since costs are directly associated to the amount of resources a provider is utilizing service providers typically achieve higher utilization and profits by multiplexing workloads from different users. The goal of this thesis is to design a solution for multiplexing ML inference workloads on GPUs, in order to increase resource utilization and adhere to SLAs of users.

##### Required Skills
Normally, the skills required for successfully taking up any of the subjects below, you should have a good grip on at roughly three of the following skills:

- Operating Systems and Networks
- Database Systems 
- Parallel Programming
- Linear Algebra
- Distributed Systems
- Cluster computing (and tools like SSH, command-line)
- Implementations of MapReduce (e.g., Apache Spark/Flink/Hadoop)

Good knowledge of a JVM-based language like Java or Scala as well as frameworks like like Akka, Netty as well as systems like Tensorflow, ScalaPACK, BLAS libraries, Python Pandas, etc. will be really handy!