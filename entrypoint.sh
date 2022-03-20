#!/bin/bash

cd /app

eval uvicorn api.app:app --reload --host 0.0.0.0 --port 5000