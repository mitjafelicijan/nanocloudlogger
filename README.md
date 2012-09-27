NanoCloudLogger
===============

Simple cloud based logger for devices like Arduino.

General information
-----------------

Nano logger provides user to easily store data in a cloud based environment without having to write any code on server side. Idea behind this is that every user can store his data (POST method) in his own stream (usually different stream id for each application) and then access data via basic GET method.

The reason behind this project is I needed simple solution for prototyping and I didn't want to write web services every time when I needed to store data remotely.

This tool is for prototyping use only. It was not intended to be used commercially.

Each stream has its own id and can store x number of inputs. Inputs in this case can be sensor data (examples below). This is especially useful for Arduino developers or any kind of telemetry projects.

Server side code is written in Python on top of Google App Engine. Tested and developed on Google App engine v1.7.2.

In example below I will demonstrate how to use this tool on a project where I have two sensors I call inputs (temperature, photocell) hooked up on a Arduino. Lets assume I am running Google App Engine locally (http://localhost:8080/)

Application is located in src/loggergae.

		python /path-to-your-gae-dir/dev_appserver.py /path-to-nano-logger-dir/src/loggergae
		
		If you are using Windows or Mac please check Google App Engine website on information how to run apps.

If you point your browser to (eg http://localhost:8080) after you run application help is displayed.

Initializing stream
-----------------

All you need to do to initialize stream is to give it an ID. Stream ID is alphanumerical string. Streams are read/write and are public. No authentication is needed for accessing and modifying stream. You can add inputs as you go.

		Stream example names:
		
		application1
		my_sensor_stream
		home_automation


Reading data stream
-----------------

		Example:	http://localhost:8080/api/get?stream=my_sensor_stream
		API url:	/api/get
		Formats:	json, csv
		Method:		GET
		Returns:	array of values

Parameters

		stream	Stream identifier.
		lastid	Only outputs records with biggers id than lastid. Useful when fetching realtime data from service and you only need latest results.
		format	Defines type of response output.
		limit	Limits number of output records.

Examples of usage:

		http://localhost:8080/api/get?stream=my_sensor_stream
		http://localhost:8080/api/get?stream=my_sensor_stream&format=json
		http://localhost:8080/api/get?stream=my_sensor_stream&lastid=50&limit=5&format=csv 

Examples of response:

		JSON
		[{ "input": "temperature", "data": "28", "id": 6, "datetime": "2012-09-27 00:54:00.441780" }, 
		{"input": "photocell", "data": "897", "id": 5, "datetime": "2012-09-27 00:54:00.439565" }]
		
		CSV
		6,2012-09-27 00:54:00.441780,temperature,28
		5,2012-09-27 00:54:00.439565,photocell,897 

Adding tool data stream
--------------------

		Examples:	http://localhost:8080/api/set?stream=my_sensor_stream
		API url:	/api/set
		Method:		POST
		Returns:	status

Examples of usage:

		http://localhost:8080/api/set?stream=my_sensor_stream
		
		POST varibles with this request:
		key            value
		--------------------------------
		temperature    28
		photocell      755
		...


