<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>




<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h1 align="center">GOLF STATS APP</h1>

  <p align="center">
    IN DEVELOPMENT
    <br />
    <br />
    This app It will utilize a Flask-Python Backend and a Vite-React Frontend to provide an experience where user’s track golf statistics from both play and practice to improve their performance.
    <br />
    <a href='https://github.com/azimmerman17/golf-stats-app'><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/azimmerman17/golf-stats-app">Explore App</a>
    ·
    <a href='https://docs.google.com/forms/d/1uQV9O5uHvIFPDLIiv-nTHkvaat4kdOin-ikKIneNxII/viewform?edit_requested=true'>Report Bug or Request Feature</a> -->
  </p>
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <!-- <a href="#getting-started">Getting Started</a> -->
      <!-- <ul> -->
        <!-- <li><a href="#prerequisites">Prerequisites</a></li> -->
        <!-- <li><a href="#installation">Installation</a></li> -->
       <!-- </ul> -->
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <!-- <li><a href="#license">License</a></li> -->
    <!-- <li><a href="#contact">Contact</a></li> -->
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
# About The Project

This app 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



## Built With

<!-- [![Vite][Vite]][Vite-url] -->
<!-- [![React][React.js]][React-url] -->
<!-- [![React Router][React-Router]][React-Router-url] -->
<!-- [![Bootstrap][Bootstrap.com]][Bootstrap-url] -->
<!-- [![ChartJS][ChartJs.com]][ChartJS-url] -->
[![Python][Python]][Python-url]
[![Flask][Flask]][Flask-url]
[![SQLAlchemy][SQLAlchemy]][SQLAlchemy-url]


<!-- [![PostgreSQL][PostgreSQL]][Postgres-url] -->
<!-- [![Sequelize][Sequelize]][Sequelize-url] -->
<!-- [![Vercel][Vercel]][Vercel-url] -->
<!-- [![Postman][Postman]][Postman-url] -->
<!-- Use Postman for the API later?  -->


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->


<!-- USAGE EXAMPLES -->
# Usage


## Frontend User 

Frontend development, not started

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

## Backend

### Tables

#### FACILITY

This table will hold data concerning each golf facility with a golf course.  Golf facilities can have multiple courses. 

| NAME | DATA TYPE | UNIQUE | NOT NULL | PRIMARY KEY | DEFAULT | FOREIGN KEY | CONSTRAINTS | DESCRIPTION
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: | --- |
| FACILITY_ID | INTEGER | X | X | X | | | | ID for the facility |
| NAME | VARCHAR(100) | | | X | | | | Name of the facility |
| HANDLE | VARCHAR(25) | X | X | | | | | Url endpoint for facility |
| CLASSIFICATION | ENUM | | X | | O | | | Type and access for facility |
| COURSE_COUNT | INTEGER | | X | | 1 | | >0 | Number of courses at the facility |
| ESTABLISHED | INTEGER | | | | | | >1400 & <=today | Year the facility was opened |
| WEBSITE | VARCHAR(100) | | | | | | | Facility website |
| ADDRESS | VARCHAR(100) | | | | | | | Facility mailing address|
| CITY | VARCHAR(50) | | | | | | | Facility City |
| STATE | VARCHAR(3) | | | | | | |State/Providence Code of the facility (USA/Canada Only) |
| COUNTRY | VARCHAR(6) | | | | | | | Facility country code, to display the country/state flag|
| GEO_LAT | FLOAT | | | | | | >-90 & <90 | Factility Latitude Coordinate |
| GEO_LON | FLOAT | | | | | | >-180 & <180 | Factility Longitude Coordinate |
| CREATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was created |
| UPDATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was last updated |

CLASSIFICATION ENUM VALUE CODES

| Key |	Value |
| :-: | :-: |
| D |	Daily-Fee |
| P |	Private |
| R |	Resort |
| M |	Municipal |
| S |	Semi-Private |
| O |	Other |

#### COURSE

This table will hold data concerning each golf course.  Courses may only attach to 1 facility, if multiple facilities share a golf course, the course attach to the primary facility.  

| NAME | DATA TYPE | UNIQUE | NOT NULL | PRIMARY KEY | DEFAULT | FOREIGN KEY | CONSTRAINTS | DESCRIPTION
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: | --- |
| COURSE_ID | INTEGER | X | X | X | | | | ID for the course |
| FACILITY_ID | INTEGER | | X | | | FACILITY.FACILITY_ID | | ID for the facility the course is attached |
| NAME | VARCHAR(100) | | | | | | | Name of the course, can be null for courses with 1 course |
| HOLE_COUNT | INTEGER | | X | | 18 | | >0 & <=18 | Number of holes on the course |
| ESTABLISHED | INTEGER | | | | | | >1574 & <=today | Year the course was opened |
| ARCHITECT | VARCHAR(100) | | | | | | | Course Designer(s) |
| CREATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was created |
| UPDATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was last updated |

#### TEE

This table will hold data concerning each tee set on golf courses.  Tees can only attach to a single course.  

| NAME | DATA TYPE | UNIQUE | NOT NULL | PRIMARY KEY | DEFAULT | FOREIGN KEY | CONSTRAINTS | DESCRIPTION
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: | --- |
| TEE_ID | INTEGER | X | X | X | | | | ID for the tee set |
| COURSE_ID | INTEGER | | X | | | COURSE.COURSE_ID | |ID for the course the tee is attached |
| NAME | VARCHAR(100) | | X | | | | | Name of the tee, cannot be null.  Should be descriptive based on the tee markers presented by the course. |
| HOLE_COUNT | INTEGER | | X | | 18 | | >0 & <=18 | Number of holes on this tee set |
| YARDAGE | INTEGER | | X | | 7200 | | >0  | Length of the course from this tee set in yards  |
| METERS | INTEGER | | X | | 6500 | | >0 | Length of the course from this tee set in meters |
| CREATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was created |
| UPDATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was last updated |

#### RATINGS

This table will hold data concerning the ratings for each tee.  Ratings can only attach to a single tee. Most courses will have 3 ratings (Full 18 holes, first 9 holes, and last 9 holes).  Some courses have routing that lends itself to have unique ratings, these ratings should follow the GHIN rating name and be manually added.

| NAME | DATA TYPE | UNIQUE | NOT NULL | PRIMARY KEY | DEFAULT | FOREIGN KEY | CONSTRAINTS | DESCRIPTION
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: | --- |
| RATING_TEE | INTEGER | X | X | X | | | | ID for the rating |
| TEE_ID | INTEGER | | X | | | TEE.TEE_ID | |ID for the tee the rating is attached |
| NAME | VARCHAR(50) | | X | | | | | Name of the rating, cannot be null.  Most common are Full, Front, and Back. |
| HOLE_COUNT | INTEGER | | X | | 18 | | =9 OR =18 | Number of holes for this rating |
| GENDER | ENUM | | X | | 'M' | | | Gender for the rating |
| START_HOLE | INTEGER | | X | | 1 | | >=1 & <=18 & <=HOLE_COUNT | Number of holes for this rating |
| COURSE_RATING | FLOAT | | X | | | | >0 | The score a scratch player, with a Handicap Index of 0.0, should achieve on a golf course under normal course and weather conditions |
| SLOPE | INTEGER | | X | | | | >=55 & <=155 | The relative difficulty of a golf course for players who are not scratch players compared to those who are scratch players |
| PAR | INTEGER | | X | | | | >=27 & <=80 | The score that an expert player would be expected to achieve on a golf course under normal course and weather conditions |
| BOGEY_RATING | FLOAT | | | | | | >0 | The score a bogey player, with a Handicap Index of 20.0, should achieve on a golf course under normal course and weather conditions |
| EFFECTIVE_DATE | DATE | | X | | CURRENT_DATE | | | Date the record is effectively active |
| CREATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was created |
| UPDATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was last updated |

#### HOLE

This table will hold data concerning the holes for each tee.  Holes can only attach to a single tee. 

Since golf courses typically have multiple tees, a row of data should be added for each hole from each sets of tees, to account for the differences for the hole for each tee set.  Example: An 18 hole course with 4 sets of tees, should create 72 different hole row.

It is a best practice to have both the Male and Female PAR and SI values for each row.  However, if the tee is not rated for either male or female, there should not be an issue as it is unlikely that scores will be posted from those tees.  If new ratings are added, PAR and SI values should be audited for accuracy.

| NAME | DATA TYPE | UNIQUE | NOT NULL | PRIMARY KEY | DEFAULT | FOREIGN KEY | CONSTRAINTS | DESCRIPTION
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: | --- |
| RATING_ID | SERIAL | x | x | x | | | | ID for the hole |
| TEE_ID | INTEGER | | x | | | TEE.TEE_ID | | | ID for the tee the hole is attached |
| NUMBER | INTEGER | | x | | | | > 0 and <= 18 | Hole Number of the Golf Course
| YARDS | INTEGER | | x | | | | > 0 and <= 999 | Hole Length (Yards) |
| METERS | INTEGER | | x | | | | > 0 and <= 999 | Hole Length (Meters) |
| PAR_MALE | INTEGER | | | | | | >= 3 and <= 6 | The score that an expert male player would be expected to make for a given hole |
| SI_MALE | INTEGER | | | | | | > 0 and <= 18 | The value assigned to each hole on a golf course to indicate where handicap strokes are given or received for male golfers |
| PAR_FEMALE | INTEGER | | | | | | >= 3 and <= 6 | The score that an expert male player would be expected to make for a given hole |
| SI_FEMALE | INTEGER | | | | | | > 0 and <= 18 | The value assigned to each hole on a golf course to indicate where handicap strokes are given or received for female golfers |
| EFFECTIVE_DATE | DATE | | X | | CURRENT_DATE | | | Date the record is effectively active |
| CREATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was created |
| UPDATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was last updated |

#### HOLE

This table will hold data concerning the geographic coordinates for each hole.  Each hole wil only have 1 record, and will be used in the mapping of the course.

| NAME | DATA TYPE | UNIQUE | NOT NULL | PRIMARY KEY | DEFAULT | FOREIGN KEY | CONSTRAINTS | DESCRIPTION |
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: | --- |
| HOLE_GEO_ID | SERIAL | x | x | x |  |  |  | Unique ID for hole, auto generated at creation |
| COURSE_ID | INTEGER | | X | | | COURSE.COURSE_ID | |ID for the course the hole is attached |
| HANDLE | INTEGER | X | X | | | | | Handle of the course - could be different from facility
| NUMBER | INTEGER | | |  | | |  | Number of the Hole |
| TEE_LAT | FLOAT | | | | | | <90 and >-90 | Latitude Coordinate of the Tee |
| TEE_LON | FLOAT | | | | | | <180 and >-180 | Longitude Coordinate of the Tee |
| DL_LAT | FLOAT | | | | | | <90 and >-90 | Latitude Coordinate of the Dog Leg Corner |
| DL_LON | FLOAT | | | | | | <180 and >-180 | Longitude Coordinate of the Dog Leg Corner |
| DL2_LAT | FLOAT | | | | | | <90 and >-90 | Latitude Coordinate of the Second Dog Leg Corner |
| DL2_LON | FLOAT | | | | | | <180 and >-180 | Longitude Coordinate of the Second Dog Leg Corner |
| CGREEN_LAT | FLOAT | | | | | | <90 and >-90 | Latitude Coordinate of the Center of the Green |
| CGREEN_LON | FLOAT | | | | | | <180 and >-180 | Longitude Coordinate of the Center of the Green |
| FGREEN_LAT | FLOAT | | | | | | <90 and >-90 | Latitude Coordinate of the Front of the Green |
| FGREEN_LON | FLOAT | | | | | | <180 and >-180 | Longitude Coordinate of the Front of the Green |
| BGREEN_LAT | FLOAT | | | | | | <90 and >-90 | Latitude Coordinate of the Back of the Green |
| BGREEN_LON | FLOAT | | | | | | <180 and >-180 | Longitude Coordinate of the Back of the Green |
| ZOOM | INTEGER | | | | | | <= 20 and > 0 | Default Tile Zoom for Map |
| ROTATION | FLOAT | | | | | | <360 and >=0 | Rotation of Map to have the hole up and down |
| GREEN_DEPTH | FLOAT | | | | | | | Depth of Green |
| CREATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was created |
| UPDATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was last updated |

***For the most accurate golf course and facility related data, consult the USGA, GHIN, and facility websites.***

#### USERS

This table stores the user profile and and settings data.  

| NAME | DATA TYPE | UNIQUE | NOT NULL | PRIMARY KEY | DEFAULT | FOREIGN KEY | CONSTRAINTS | DESCRIPTION
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: | --- |
| USER_ID | SERIAL | x | x | x |  |  |  | Unique ID for user, auto generated at creation |
| USERNAME | VARCHAR(25) | x | x |  |  |  |  | Unique name, generated by the user |
| FIRST_NAME | VARCHAR(25) |  | x |  |  |  |  | First Name as provided by the user |
| LAST_NAME | VARCHAR(25) |  | x |  |  |  |  | Last Name as provided by the user |
| EMAIL | VARCHAR(50) | x | x |  |  |  |  | Unique email, generated by the user |
| GENDER | ENUM |  | x |  | P |  |  | Gender as provided by the user (M, F, N, P) |
| DOB | DATE |  |  |  |  |  |  | User's Date of Birth |
| HOME_FACILITY | INTEGER |  |  |  |  | FACILITY.FACILITY_ID |  | The course the user primarlly plays. |
| NATIONALITY | VARCHAR(6) |  |  |  |  |  |  | The country the user lives, most will be 2 letter code, GB will have 6, to show the flag |
| PLAYER_TYPE | EMUN |  |  |  |  |  |  | The user's golfer type (A, C, P, TP)  |
| UNITS | EMUN |  |  |  |  |  |  | The user's preffered unit of measurement (Y, M)  |
| ROLE | EMUN |  |  |  |  |  |  | The user's role for access (basic, vip, admin)  |
| CREATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was created |
| UPDATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was last updated |

GENDER ENUM VALUE CODES

| Key |	Value |
| :-: | :-: |
| M |	Male |
| F |	Female |
| N |	Non-Binary/Other |
| P |	Prefer Not To Say |

PLAYER_TYPE ENUM VALUE CODES

| Key |	Value |
| :-: | :-: |
| A |	Amatuer |
| C |	College |
| P |	Professional |
| TP |	Tour Professional |

UNITS ENUM VALUE CODES

| Key |	Value |
| :-: | :-: |
| Y |	Yards |
| M |	Meters |

***Home Facility could become a separate table for users with multiple home courses***

#### USER_AUTH

This table stores the user's authentication information.  

| NAME | DATA TYPE | UNIQUE | NOT NULL | PRIMARY KEY | DEFAULT | FOREIGN KEY | CONSTRAINTS | DESCRIPTION
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: | --- |
| AUTH_ID | SERIAL | x | x | x |  |  |  | Unique ID for the authetication row, auto generated at creation |
| USER_ID | INTEGER |  | x |  |  | USER.USER_ID |  | Unique ID for user, auto generated at creation |
| SALT | VARCHAR(50) |  | x |  |  |  |  | Salt value for the user authetication |
| PASSWORD_HASH | VARCHAR(100) |  | x |  |  |  |  | User's hashed password |
| ACTIVE | VARCHAR(1) |  | x |  | A |  |  | Indicator if the hashed password is active |
| GUID_TOKEN | VARCHAR(50) |  | x |  |  |  |  | Guid token for account security actions |
| GUID_EXPIRE | TIMESTAMP | | X | | NOW() | | | Timestamp guid token expires |
| CREATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was created |
| UPDATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was last updated |

### Blueprints

Blueprints are  still in development

#### FACILITY

This Blueprint is used to perform CRUD actions for data assoicated with golf facilities and courses. Documentaion of specific Endpoints are being developed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- 


<!-- See the [open issues](https://github.com/azimmerman17/golf-stats-app/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->


<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


Additionally you can utilize the [Support Form][Support-url] to report any bugs or offer suggestions and feedback

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- CONTACT -->
<!-- ## Contact

Andrew Zimmerman - azimmerman@pga.com

Project Link: [https://github.com/azimmerman17/golf-stats-app](https://github.com/azimmerman17/golf-stats-app) -->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

This app is still a work in progress and is not ready for use

<p align="right">(<a href="#readme-top">back to top</a>)</p>














<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- BADGES -->
[contributors-shield]: https://img.shields.io/github/contributors/azimmerman17/golf-stats-app.svg?style=for-the-badge
[contributors-url]: https://github.com/azimmerman17/golf-stats-app/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/azimmerman17/golf-stats-app.svg?style=for-the-badge
[forks-url]: https://github.com/azimmerman17/golf-stats-app/network/members
[stars-shield]: https://img.shields.io/github/stars/azimmerman17/golf-stats-app.svg?style=for-the-badge
[stars-url]: https://github.com/azimmerman17/golf-stats-app/stargazers
[issues-shield]: https://img.shields.io/github/issues/azimmerman17/golf-stats-app.svg?style=for-the-badge
[issues-url]: https://github.com/azimmerman17/golf-stats-app/issues
[license-shield]: https://img.shields.io/github/license/azimmerman17/golf-stats-app.svg?style=for-the-badge
[license-url]: https://github.com/azimmerman17/golf-stats-app/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/azimmerman17

<!-- PACKAGES -->
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org
[Flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/stable/
[SQLAlchemy]: https://img.shields.io/badge/SQLAlchemy-F9DC3E?style=for-the-badge&logo=sqlalchemy&logoColor=black
[SQLAlchemy-url]: https://www.sqlalchemy.org/