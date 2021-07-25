# Chenhao's Stock Price Subscription system
A local web app to subscribe to your automated mailing list with updated stock ticker prices. Developed using Django.

You may check it hosted by Heroku <a href='https://stock-subscription.herokuapp.com/'>here</a>. 

## To start the app locally

- Clone the git repository on your local machine. 
- Execute `cd src && python manage.py runserver` in the directory of this repository. 
- *It is highly recommended that you run this app on a virtualenv.*

Note that the sending email features will not work if you run this project locally, as AWS access keys are not inculded on this remote repository due to security reason as specified by AWS. 
