drop table if exists user;
drop table if exists code;
drop table if exists trophy;
drop table if exists archivement;
drop table if exists comment;

--Join tables
drop table if exists user_trophy;
drop table if exists user_archivement;
drop table if exists user_code;

--View
drop view if exists top3;


create table user(
id integer primary key AUTOINCREMENT,
nombre_completo text,
nombre_usuario text,
pass text,
score integer
);

create table trophy(
id integer primary key AUTOINCREMENT,
name text,
des text,
image text
);

create table archivement(
id integer primary key AUTOINCREMENT,
name text,
des text,
image text
);

create table code(
id integer primary key AUTOINCREMENT,
user_id integer not null references user(id),
submit_date date,
des text,
code_sample text
);

create table comment(
id integer primary key AUTOINCREMENT,
user_id integer not null references user(id),
code_id integer not null references code(id),
comment_date date,
value text
);

--Join tables
create table user_trophy(
user_id references user(id),
trophy_id references trophy(id),
win_n_times integer,
last_win date,
PRIMARY KEY (user_id, trophy_id)
);

create table user_archivement(
user_id references user(id),
archivement_id references archivement(id),
win_date date,
PRIMARY KEY (user_id, archivement_id)
);

create table user_code(
user_id references user(id),
code_id references code(id),
score integer,
PRIMARY KEY (user_id, code_id)
);

--Sample data

insert into user values(null, 'Miguel', 'chompy', 'pass', 123);
insert into user values(null, 'Nick', 'Canela', 'pass', 111);
insert into user values(null, 'Calatrava', 'calatrava', 'pass', 9000);
insert into user values(null, 'David', 'sass', 'pass', 200);
  
insert into trophy values(null, 'Sass Oro', 'Sass oro', 'img');
insert into trophy values(null, 'RetroSass', 'Retro sass', 'img');
insert into trophy values(null, 'Sass Plata', 'Plata', 'img');
insert into trophy values(null, 'Sass bronce', 'Lo mejor que te puede pasar siendo el peor', 'img');
    
insert into archivement values(null, 'Romper master', 'Romper Master', 'img');
insert into archivement values(null, 'Datatables', 'Conseguir crear datatables en local', 'img');
insert into archivement values(null, 'premio prueba', 'Premio y descripcion de prueba', 'img');
insert into archivement values(null, 'premio sass', 'Mantener la tarea 14540 mas de 30 dias', 'img');
  
insert into code values(null, 1, '10/06/2018', 'Descripcion del error', 'while(true)');
insert into code values(null, 1, '12/06/2018', 'Romper Master', 'Datatables local');
insert into code values(null, 2, '11/06/2018', 'Romper Gateway', 'error de alias');
insert into code values(null, 3, '12/06/2018', 'Otro error mas', 'test');
  
--Sample data join

insert into user_trophy values(1, 2, 3, '10/06/2018');
insert into user_trophy values(1, 4, 4, '9/06/2018');
insert into user_trophy values(2, 1, 2, '8/06/2018');
insert into user_trophy values(4, 4, 3, '7/06/2018');

insert into user_archivement values(1, 2, '10/05/2018');
insert into user_archivement values(4, 4, '9/06/2018');
insert into user_archivement values(2, 2, '1/06/2018');
insert into user_archivement values(4, 3, '7/06/2018');
  
insert into user_code values(1, 2, 5);
insert into user_code values(1, 3, 7);
insert into user_code values(2, 2, 9);
insert into user_code values(2, 3, 1);
insert into user_code values(3, 1, 1);
insert into user_code values(3, 2, 6);
insert into user_code values(3, 3, 9);
insert into user_code values(3, 4, 2);
insert into user_code values(4, 3, 4);
  
--view
CREATE VIEW top3 AS 
    SELECT u.nombre_completo AS nombre_completo, u.nombre_usuario AS nombre_usuario, u.score as score, (select name from trophy t, user_trophy ut where t.id = ut.trophy_id and ut.user_id = u.id order by ut.last_win limit 1) as last_trophy
    FROM user u
    order by score desc limit 3;
  