NanoCloudLogger
===============

Simple cloud based logger for devices like Arduino.

General information

Nano logger provides user to easily store data in a cloud based environment without having to write any code on server side. Idea behind this is that every user can store his data (POST method) in his own stream (usually different stream id for each application) and then access data via basic GET method.

The reason behind this project is I needed simple solution for prototyping and I didn't want to write web services every time when I needed to store data remotely.

This tool is for prototyping use only. It was not intended to be used commercially.

Each stream has its own id and can store x number of inputs. Inputs in this case can be sensor data (examples below). This is especially useful for Arduino developers or any kind of telemetry projects.

Server side code is written in Python on top of Google App Engine. Tested and developed on Google App engine v1.7.2.

In example below I will demonstrate how to use this tool on a project where I have two sensors I call inputs (temperature, photocell) hooked up on a Arduino. Lets assume I am running Google App Engine locally (http://localhost:8080/)

Initializing stream

All you need to do to initialize stream is to give it an ID. Stream ID is alphanumerical string. Streams are read/write and are public. No authentication is needed for accessing and modifying stream. You can add inputs as you go.

		Stream example names:
		
		application1
		my_sensor_stream
		home_automation
