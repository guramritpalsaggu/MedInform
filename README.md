## MEDINFORM
### AI Powered Multipurpose Platform for medical image analysis

- Developed CNN based Deep Learning Models that would
classify the medical images into their respective classes
based on the disease.
- Deployed our models using a web based application in which
users can upload medical image and the app will
display the results to the user.
- This would provide assistance to medical practitioners and a
reliable second opinion to people without medical
background about diseases that can be detected from
medical images or scans taken by medical professionals or
people themselves.
- This app will classify various diseases such as Tuberculosis,
Skin Cancer, Malaria, Covid-19, Pneumonia and Diabetic
Retinopathy

### Need of such a system
- Efficient and widespread testing is needed in cases of diseases that spread exponentially,
such as Malaria and Covid-19. In that case presence of online system can greatly increase
number of tests being performed and decrease the duration of test.
- In case of highly infectious diseases, an online system would greatly decrease the number
 of people that come in contact with samples. Hence reducing the front line workers in case
of highly infectious disease which would help reducing their spread.
- Since this approach just uses image in order to predict the result, in some cases this
would reduce the amount of equipment required to get results which would make it
easier to setup remote camps for those diseases and will be boost for telemedicine
sector.
- Online testing can easily be standardized which means that no matter where the test
would be done the results would be same, that removes the need for people to travel to
far away places just to get tests done.


### System Design

![alt text width = 400](https://github.com/guramritpalsaggu/Medical_Image_Analysis/blob/master/resources/dfd.png)

### Transfer Learning

Transfer learning is a machine learning method where a model
developed for a task is reused as the starting point for a model on a
second task. It is a popular approach in deep learning where
pre-trained models are used as the starting point on computer vision
and natural language processing tasks given the vast compute and time
resources required to develop neural network models on these
problems and from the huge jumps in skill that they provide on related
problems. We have used Resnet-50, VGG-16 & Inception V3 model to train our models.


### Tech Stack
- Client Side Web Application - ReactJS, JavaScript
- Server Side - Starlette + Unicorn, Keras API
- ML Models - Python, Tensorfloe, Keras , OpenCV
- The Ops - Docker Environment, Google Cloud Platform(GCP), Google Cloud Run and Build API(CI/CD)

