/* jshint unused: false */
(function(){
  'use strict';
  
  var paths = {
    tmp: 'gulptmp/',
    dest: 'electionleaflets/media/',
    src: 'electionleaflets/assets-src/',
    fonts: [],
    images: [],
    scripts: {},
    styles: [],
  };
  
  paths.styles.push(paths.src + 'stylesheets/**/*.scss');
  paths.styles.push(paths.src + 'stylesheets/**/*.css');
  paths.styles.push(paths.src + 'vendor/**/*.scss');
  paths.styles.push(paths.src + 'vendor/**/*.css');
  
  // images
  paths.images.push(paths.src + 'images/**/*');
  
  paths.fonts.push(paths.src + 'fonts/*.{otf,eot,svg,ttf,woff,woff2}');
  paths.fonts.push(paths.tmp + 'fonts/*.{otf,eot,svg,ttf,woff,woff2}');
  paths.fonts.push(paths.src + 'vendor/**/*.{otf,eot,svg,ttf,woff,woff2}');
  paths.fonts.push(paths.tmp + 'vendor/**/*.{otf,eot,svg,ttf,woff,woff2}');
  
  // scripts
  paths.scripts = {
    vendor: [
      paths.src + 'vendor/jquery/jquery.js',
      paths.src + 'vendor/masonry/index.js',
      paths.src + 'vendor/leaflet/index.js',
      // paths.src + 'vendor/handlebars/handlebars.js',
      // paths.src + 'vendor/ember/ember.js',
      // paths.src + 'vendor/ember-data/ember-data.js',
    ],
    app: [
        paths.src + 'javascript/app/app.js',
        // paths.src + 'javascript/app/routes.js',
        // paths.src + 'javascript/app/helpers/**/*.js',
        // paths.src + 'javascript/app/models/*.js',
        // paths.src + 'javascript/app/components/**/*.js',
        // paths.src + 'javascript/app/controllers/**/*.js',
        // paths.src + 'javascript/app/views/**/*.js',
        // paths.tmp + 'javascript/templates.js',
    ]
  };
  
  
  var gulp = require('gulp'),
    handlebars = require('gulp-handlebars'),
    uglify = require('gulp-uglify'),
    wrap = require('gulp-wrap'),
    declare = require('gulp-declare'),
    concat = require('gulp-concat'),
    minifyCss = require('gulp-minify-css'),
    rename = require('gulp-rename'),
    ignore = require('gulp-ignore'),
    rimraf = require('gulp-rimraf'),
    watch = require('gulp-watch'),
    imagemin = require('gulp-imagemin'),
    order = require('gulp-order'),
    templateCompiler = require('gulp-ember-template-compiler'),
    sass = require('gulp-ruby-sass');
  
  gulp.task('clean-pre', function() {
    return gulp
      .src([paths.dest, paths.tmp], {read: false})
      .pipe(ignore('node_modules/**'))
      // .pipe(rimraf());
  });
  
  gulp.task('copy-fonts', function() {
    gulp.src(paths.fonts)
      .pipe(gulp.dest(paths.dest + 'fonts/'));
  });
  
  // optimise images
  gulp.task('images', function() {
    gulp
      .src(paths.images)
      .pipe(imagemin({optimizationLevel: 5}))
      .pipe(gulp.dest(paths.dest + 'images'));
  });
  
  
  // copy & compile scss
  gulp.task('copy-sass', function() {
    return gulp
      .src(paths.styles)
      .pipe(gulp.dest(paths.tmp + 'stylesheets/'));
  });


  gulp.task('sass', function() {
    return sass(paths.tmp + 'stylesheets/main.scss', {
        lineNumbers: true,
        style: 'compact'
      })
      .on('error', function (err) { console.log('ERROR: '+err.message); })
      .pipe(gulp.dest(paths.tmp + 'stylesheets/'));
  });



  gulp.task('css', ['copy-sass', 'sass'], function() {
    gulp
      .src(paths.tmp + 'stylesheets/main.css')
      .pipe(minifyCss())
      .pipe(rename({ suffix: '.min' }))
      .pipe(gulp.dest(paths.dest + 'stylesheets/'));
  });




  // gulp.task('templates', function() {
  //   gulp.src([paths.src + 'javascript/app/templates/**/*.hbs'])
  //     .pipe(handlebars())
  //     .pipe(wrap('Handlebars.template(<%= contents %>)'))
  //     .pipe(declare({
  //        namespace: 'templates'
  //        // noRedeclare: true, // Avoid duplicate declarations
  //      }))
  //     .pipe(concat('templates.js'))
  //     .pipe(gulp.dest(paths.tmp + 'javascript/'));
  // });
  gulp.task('templates', function () {
    gulp.src(paths.src + 'javascript/app/templates/**/*.hbs')
      .pipe(templateCompiler())
      .pipe(concat('templates.js'))
      .pipe(gulp.dest(paths.tmp + 'javascript/'));
  });


  // gulp.task('source_maps', function() {
  //   gulp.src([paths.src + '/**/*.js.map'])
  //     .pipe(gulp.dest(paths.dest + 'javascript/'));
  // });
  
  gulp.task('scripts', ['templates',], function() {
    var all_scripts = paths.scripts.vendor.concat(paths.scripts.app);
    console.log(all_scripts);
    
    return gulp.src(all_scripts)
      // .pipe(uglify({ mangle: true }))
      .pipe(concat('electionleaflets.main.min.js'))
      .pipe(gulp.dest(paths.dest + 'javascript/'));
  });
  
  gulp.task('watch', function() {
    //watches SCSS files for changes
    gulp.watch(paths.src + '**/*.scss', ['css']);
 
    //watches handlebars files for changes
    gulp.watch(paths.src + 'javascript/app/templates/**/*.hbs', ['templates', 'scripts']);
   
    //watches JavaScript files for changes
    gulp.watch(paths.src + '**/*.js', ['templates', 'scripts']);
    gulp.watch(paths.tmp + '**/*.js', ['scripts']);
  });
  
  gulp.task('build', ['clean-pre', 'css', 'scripts']);
  gulp.task('default', ['images', 'copy-fonts', 'css', 'scripts', 'watch']);

})();