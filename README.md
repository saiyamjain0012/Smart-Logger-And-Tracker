# Smart-Logger-And-Tracker
ELK based smart solution for website/user logging and tracking 

## Architecture of the project included the following- 
* Elasticsearch 
* Logstash
* Kibana
* Python
* Flask Web App
* Heart Beat Module
![architecture](https://user-images.githubusercontent.com/28778579/121016919-593dd100-c7ba-11eb-8c21-76d1ea036b9a.PNG)

The sample website is built with a few functionalities mainly to demonstrate how to log data of the active user- 
![website](https://user-images.githubusercontent.com/28778579/121017620-1af4e180-c7bb-11eb-9694-eef591292b8c.PNG)

## User Logs Handling- 

The flask web app tracks the activity of the user on the website on metrics such as clicks, searches and time spent on the website. This data is pushed to Elasticsearch and using Kibana data insights are extracted for making better data decisions. 

The logs look like this- 
![ES_data](https://user-images.githubusercontent.com/28778579/121017331-c9e4ed80-c7ba-11eb-9236-dc335d6fc453.PNG)

Dashboard to get data insights- 
![dashboard_1](https://user-images.githubusercontent.com/28778579/121017415-e123db00-c7ba-11eb-9996-a26bbd58cf4d.png)
![dashboard_2](https://user-images.githubusercontent.com/28778579/121017385-d79a7300-c7ba-11eb-8123-151c9bec86d3.png)

The Uptime Tracker module runs with the HeartBeat Module in the backend along with another python flask web app and allows the user to track the status of any hosted website- 
![uptime](https://user-images.githubusercontent.com/28778579/121018119-b5552500-c7bb-11eb-9423-95ea51e94e42.PNG)

A future advancement for this would be to make a logging extension of some sort that just attaches itself to the data points to make things more quick. 

For any questions or queries please write to me at saiyamjain0012@gmail.com


