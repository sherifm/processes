# Dockerfile extending the generic Python image with application files for a
# single application. This is only used for pre- env: 2 deployments.

# The name of this image is for historical reasons 'python-compat', but it
# refers to a version of the runtime separate from the 'runtime: python-compat'
# image.

FROM gcr.io/google_appengine/python-compat

RUN apt-get update && apt-get install -y \
	stress \
	python-psutil
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
