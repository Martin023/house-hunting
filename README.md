# Project Title

Having sleepless nights looking for a house?, 
Master homes provides the easiest and most efficient house hunting help website connecting you to home owners and easy viewing of a house of your choice in any location. House features included, you can get any house that matches your taste and price. Enjoy!

## Getting Started

Follow the instructions below beginning from the prerequisites to get the project set upand running. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Django installation
* Python installatio
* pip installation
* Python code-runner 


```
visual studio,pycharm or any text editor of your choice.
```

### Installing

Clone the project or fork the repository to your github and then clone to your local machine
```
git clone https://github.com/Martin023/house-hunting
```
navigate to the parent folder of the project
```
cd/< clone location >/house-hunting
```
Install and activate a python virtual environment 
From terminal :
```
pip3 install virtual env 
virtualenv <virtual environment name>
source <virtual environment name>/bin/activate

```
Install project requirements:
```
pip3 install -r requirements.txt
```
Replace environment varibles with your own
```
    django configurations 
SECRET_KEY=

    Postgrress database configurations 
DB_NAME=
DB_USER=
DB_PASS=
DB_HOST=

    cloudinary configurations
API_KEY=
API_SECRET=
```

Run the project on a local server : The default is on port 8000
```
python3 manage.py runserver <port>

```
The project should be running on the localhost as shown below


## Running the tests

To run tests 
```
make test
```



## Deployment

Follow [this] link for on deploying notes.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Cloudinary](https://cloudinary.com/) - Images storage platform
* [Postgressql](https://www.postgresql.org/) - Database used

## Contributing

Create a request on the [contrubutions] link.
Once granted access create a new branch
```
git branch <branchname>
```
Code Away!
## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/Martin023/house-hunting). 

## Authors

* **Martin Maina** - [martin023](https://github.com/martin023)

See also the list of [contributors](https://github.com/Martin023/house-hunting/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Maryann](https://github.com/maryann23) -Technical Mentor
* Inspiration - masterhomes.co.ke 

