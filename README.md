# BlindSqliCookieParam

This Python script is designed to test web applications for Blind SQL Injection vulnerabilities, specifically through cookie parameters, by exploiting timing attacks. The goal is to attempt reading a specified Linux file, demonstrating the potential for data exfiltration in vulnerable applications.

## Overview
Blind SQL Injection (SQLi) vulnerabilities exist when an application fails to properly sanitize user input for SQL queries. Unlike traditional SQLi, blind SQLi doesn't return direct query results but can be detected through side-channel information, such as response times. This script automates the detection process by measuring how long the server takes to respond to crafted requests that cause the database to perform time-consuming operations if the injection is successful.

## Features
Automated testing for Blind SQL Injection via cookie parameters.
Utilizes timing attacks to infer database information.
Capable of reading files from a Linux system if the database has the necessary permissions.
Configurable for different targets, cookies, and payloads.

### Requirements
Python 3.x
Requests library

### Warning
This tool is intended for educational purposes and ethical testing only. Always seek permission before testing a web application for vulnerabilities.



