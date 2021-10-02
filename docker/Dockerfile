FROM php:7.4-apache

RUN apt-get update && apt-get install -y --no-install-recommends \
  libfreetype6-dev  libjpeg62-turbo-dev libpng-dev imagemagick

RUN docker-php-ext-install mysqli pdo pdo_mysql && a2enmod rewrite
RUN docker-php-ext-configure gd --with-freetype --with-jpeg
RUN docker-php-ext-install -j$(nproc) gd exif

RUN cp /usr/local/etc/php/php.ini-production /usr/local/etc/php/php.ini
RUN echo "error_reporting = E_COMPILE_ERROR|E_RECOVERABLE_ERROR|E_ERROR|E_CORE_ERROR;" >> /usr/local/etc/php/php.ini
