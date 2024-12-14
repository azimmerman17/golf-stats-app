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

This table will hold data concerning each golf facility with a golf course

| NAME | DATA TYPE | UNIQUE | NOT NULL | PRIMARY KEY | DEFAULT | FOREIGN KEY | CONSTRAINTS | DESCRIPTION
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: | --- |
| FACILITY_ID | INTEGER | X | X | X | | | | ID for the facility |
| NAME | VARCHAR(100) | | | X | | | | Name of the facility |
| HANDLE | VARCHAR(25) | X | X | | | | | Url endpoint for facility |
| CLASSIFICATION | ENUM | | X | | O | | | Type and access for facility |
| COURSE_COUNT | INTEGER | | X | | 1 | | >0 | Number of course at the facility |
| ESTABLISHED | INTEGER | | | | | | >1400 & <=today | Year the facility was opened |
| WEBSITE | VARCHAR(100) | | | | | | | Facility website |
| ADDRESS | VARCHAR(100) | | | | | | | Facility mailing address|
| CITY | VARCHAR(50) | | | | | | | Facility City |
| STATE | VARCHAR(3) | | | | | | |State/Providence Code of the facility (USA/Canada Only) |
| COUNTRY | VARCHAR(3) | | | | | | | Facility 3 letter country code |
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

This table will hold data concerning each golf course

| NAME | DATA TYPE | UNIQUE | NOT NULL | PRIMARY KEY | DEFAULT | FOREIGN KEY | CONSTRAINTS | DESCRIPTION
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: | --- |
| COURSE_ID | INTEGER | X | X | X | | | | ID for the course |
| FACILITY_ID | INTEGER | | X | | | FACILITY.FACILITY_ID | | ID for the facility the course is acctached |
| NAME | VARCHAR(100) | | | | | | | Name of the course, can be null for courses with 1 course |
| HOLE_COUNT | INTEGER | | X | | 18 | | >0 & <=18 | Number of holes on the course |
| ESTABLISHED | INTEGER | | | | | | >1574 & <=today | Year the course was opened |
| ARCHITECT | VARCHAR(100) | | | | | | | Course Designer |
| CREATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was created |
| UPDATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was last updated |

#### TEE

This table will hold data concerning each tee set on golf courses

| NAME | DATA TYPE | UNIQUE | NOT NULL | PRIMARY KEY | DEFAULT | FOREIGN KEY | CONSTRAINTS | DESCRIPTION
| --- | --- | :-: | :-: | :-: | :-: | :-: | :-: | --- |
| TEE_ID | INTEGER | X | X | X | | | | ID for the tee set |
| COURSE_ID | INTEGER | | X | | | COURSE.COURSE_ID | |ID for the course the tee is attached |
| FACILITY_ID | INTEGER | | X | | | FACILITY.FACILITY_ID | | ID for the facility the tee_set is attached |
| NAME | VARCHAR(100) | | X | | | | | Name of the tee, cannot be null |
| HOLE_COUNT | INTEGER | | X | | 18 | | >0 & <=18 | Number of holes on this tee set |
| YARDAGE | INTEGER | | X | | 7200 | | >0  | Length of the course from this tee set in yards  |
| METERS | INTEGER | | X | | 6500 | | >0 | Length of the course from this tee set in meters |
| CREATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was created |
| UPDATED_AT | TIMESTAMP | | X | | NOW() | | | Timestamp record was last updated |

### End Points

End points not yet developed

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