---
layout: default
title: "Big Data Processing | Streaming Assignment"
---
<br/>

### Streaming Data Analytics


#### Dataset
In this exercise we are going to use the [Github event timeline](https://api.github.com/events) in order to gain some real-time insights on the development of Github projects. For the analysis we are going to use the [Apache Flink](http://flink.apache.org) system - the leading open source system for stream analysis. For an overview of how Flink works, you can take a look at the paper ["Apache Flink: Stream and Batch Processing in a Single Engine"](http://asterios.katsifodimos.com/assets/publications/flink-deb.pdf) (note that the API might have changed since the paper was published - the principles, though, remain the same). For an up-to-date tutorials, etc., you can use [Flink's training material](http://training.data-artisans.com/).

We will use the [Github events](https://developer.github.com/v3/activity/events/types/), so, please head to the documentation page in order to see some examples before we continue. 

Unlike the [batch processing assignment you had to implement in Spark](http://gousios.gr/courses/bigdata/assignment-spark.html), in this example the data is considered to be *unbounded*. This means that the dataset never ends; one can hook into the events API of Github with a continuous query, and receive data (and query results) infinitely. In order to simplify development, in this exercise we will focus on a subset of 5 days worth of data stored in a file. You can download the dataset from [here](https://www.dropbox.com/s/6a592zxb67dtkqp/github-okt1-5.10.2017.gz?dl=0) (~500MBs compressed - no need to decompress).

This assignment will give you a total of 110 points.

#### Setup Your Development Environment
Please follow [this guide](http://training.data-artisans.com/devEnvSetup.html) in order to setup your development environment. Before you move on to creating your own Flink programs, make sure that you can run the bundled examples that Flink ships with.



#### Task #1: Parsing JSON events into Flink tuples (10pts)
You can find a description of all event-types [here](https://developer.github.com/v3/activity/events/types/). Your data source will have to read each file line, parse the content of that line (i.e., the serialized JSON object) and emit a stream of Java/Scala JSON objects. For instance, below you find a [commit comment creation event](https://developer.github.com/v3/activity/events/types/#commitcommentevent) by a given `user` and on a given `repository`. The `comment/created_at` field, gives us the time when the commit comment was created.

```json
{
  "action": "created",
  "comment": {
    "url": "https://api.github.com/repos/baxterthehacker/public-repo/comments/11056394",
    "html_url": "https://github.com/baxterthehacker/public-repo/commit/9049f1265b7d61be4a8904a9a27120d2064dab3b#commitcomment-11056394",
    "id": 11056394,
    "user": {
      "login": "baxterthehacker",
      "id": 6752317,
      "url": "https://api.github.com/users/baxterthehacker",
      ...
      "type": "User",
      "site_admin": false
    },
    ...
    "commit_id": "9049f1265b7d61be4a8904a9a27120d2064dab3b",
    "created_at": "2015-05-05T23:40:29Z",
    "updated_at": "2015-05-05T23:40:29Z",
    "body": "This is a really good change! :+1:"
  },
  "repository": {
    "id": 35129377,
    "name": "public-repo",
    ...
    "owner": {
      "login": "baxterthehacker",
      "id": 6752317,
      "url": "https://api.github.com/users/baxterthehacker",
      ...
    },
    ...
    "created_at": "2015-05-05T23:40:12Z",
    "updated_at": "2015-05-05T23:40:12Z",
    "pushed_at": "2015-05-05T23:40:27Z",
    ...
  },
  "sender": {
  ...
  }
}
```

#### Task #2: Filtering events of interest (10pts)
In this task you will have to keep only the events that are of interest to us. More specifically, you will have to receive the objects and decide what those events represent. We will be using only the following event-types:
- [IssuesEvent](https://developer.github.com/v3/activity/events/types/#issuesevent), i.e., when a Github issue is opened, closed, etc.
- [PushEvent](https://developer.github.com/v3/activity/events/types/#pushevent), i.e., when a `git push` has been done. This contains all the commits that the push contains.
- [RepositoryEvent](https://developer.github.com/v3/activity/events/types/#repositoryevent), i.e., when a repository is created, made public, edited, etc.

Subsequently, each of these objects will have to be given an event time (see below) so that Flink's windowing operators can assign each event to different windows.

#### Task #3: Defining Event-time (20pts)
The first part of the assignemnt is to define the event-time of each of the events. You can refer to [these slides](http://training.data-artisans.com/dataStream/time.html) for more information on how Flink treats time (and watermarks).

Remember: the event-time of an event is the time in which the event was generated, not the time that the event has reached the streaming system.

Roughly speaking, you will have to create [an extractor](https://ci.apache.org/projects/flink/flink-docs-release-1.3/dev/event_timestamp_extractors.html) for each event type, which will assign an event-time on each event of interest. For instance, a [creation event](https://developer.github.com/v3/activity/events/types/#createevent) contains a `created_at` field, stating when that repository was created. Note that the events from the github event timeline do not necessarily come in-order.

In the subsequent tasks, you will have to create one Flink job for each of the following queries. Please make sure that you reuse the code (e.g., the data sources and time assignment) you have written for the previous tasks.

#### Task #4: Computing Aggregates over (Sliding) Windows (30pts)

- Every hour, report the count the unique issues that have been opened per repository during the last 2 days (10pts).
- Every minute, report the number of repositories that have been created that very minute (10pts).
- Count the number of issues per project, which have not received any updates (i.e., closed, opened, etc.) for more than one day. Is this a session window?(10pts) 

#### Task #5: Extracting Patterns (30pts)

For the following tasks you will have to use the Flink CEP library. A nice introduction can be found [here](https://data-artisans.com/blog/complex-event-processing-flink-cep-update).

- Output all repositories that have been switched from private to public (15pts).
- Count all issues that have been opened, closed, and re-opened in less than 48 hours (15pts).
