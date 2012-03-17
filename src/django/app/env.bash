#!/bin/bash


export PORT=8900

RUN()
{
    python manage.py runserver 0.0.0.0:$PORT
}
