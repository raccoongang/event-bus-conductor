'use strict';

const gulp = require('gulp'),
    sass = require('gulp-sass')(require('sass')),
    autoprefixer = require('gulp-autoprefixer'),
    concat = require('gulp-concat'),
    cleanCSS = require('gulp-clean-css'),
    sourcemaps = require('gulp-sourcemaps');

gulp.task('sass', () => {
    return gulp.src('event_bus_conductor/static/event_bus_conductor/sass/**/*')
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(sass())
        .pipe(autoprefixer({ cascade: false, grid: true }))
        .pipe(cleanCSS())
        .pipe(concat('bundle.min.css'))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('event_bus_conductor/static/event_bus_conductor/css'))
});

gulp.task('watch', () => {
    gulp.watch(
        'event_bus_conductor/static/event_bus_conductor/sass/**/*', gulp.parallel('sass')
    );
});

gulp.task('default', gulp.series('sass', 'watch'));
gulp.task('build', gulp.series('sass'));
