<!-- manual -->

## Your Tasks

Modify the doctor application discussed in this chapter so that it tracks clients by name and history. A `Doctor` object has its own history list of a patient’s inputs for
generating replies that refer to earlier conversations, as discussed in Chapter 5.

A `Doctor` object (in the file **doctor.py**) is now associated with a patient’s name. The client application (in the file **doctorclient.py**) takes this name as input and sends it to the client handler (in the file **doctorclienthandler.py**) when the patient connects.

Update the **doctorclienthandller.py** file so the`DoctorClientHandler` class checks for a pickled file with the patient’s name as its filename ("**[patient name].dat**”). If that file exists, it will contain the patient’s history, and the client handler loads the file to create the `Doctor` object.

Otherwise, the patient is visiting the doctor for the first time, so the client handler creates a brand-new `Doctor` object. When the client disconnects, the client handler pickles the `Doctor` object in a file with the patient’s name. (LO: 12.1, 12.3)

> This lab follows a client server model. In order for the client program to connect to the server the following steps must be taken:

1. Enter `python3 doctorserver.py` into the first **Terminal**.
2. Open a new terminal tab by clicking the '**+**' at the top of the terminal pane.
3. Enter `python3 doctorclient.py` into the second **Terminal**.

> The client code will now be able to establish a connection to the server.

## Instructions
