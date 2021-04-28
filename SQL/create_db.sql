CREATE TABLE "shedule" (
	"id" serial NOT NULL,
	"audience" int,
	"class" int,
	"day" int,
	"faculty" int,
	"group_" int,
	"subject" int,
	"teacher" int,
	"type_of_class" int,
	"week" int,
	"subgroup" int,
	CONSTRAINT "shedule_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "days" (
	"id" serial NOT NULL,
	"day" TEXT NOT NULL,
	CONSTRAINT "days_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "weeks" (
	"id" serial NOT NULL,
	"parity" TEXT NOT NULL,
	CONSTRAINT "weeks_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "groups_" (
	"id" serial NOT NULL,
	"group_" TEXT NOT NULL,
	"course" int NOT NULL,
	"faculty" int NOT NULL,
	CONSTRAINT "groups_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "teachers" (
	"id" serial NOT NULL,
	"full_name" TEXT NOT NULL,
	"position" int,
	CONSTRAINT "teachers_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "facultys" (
	"id" serial NOT NULL,
	"faculty" TEXT NOT NULL,
	"abbreviation" TEXT NOT NULL,
	CONSTRAINT "facultys_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "classes" (
	"id" serial NOT NULL,
	"number" int NOT NULL,
	"start_time" TIME NOT NULL,
	"end_time" TIME NOT NULL,
	"time_str" TEXT NOT NULL,
	CONSTRAINT "classes_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "audiences" (
	"id" serial NOT NULL,
	"name" TEXT NOT NULL,
	CONSTRAINT "audiences_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "subjects" (
	"id" serial NOT NULL,
	"subject" TEXT NOT NULL,
	CONSTRAINT "subjects_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "type_of_classes" (
	"id" serial NOT NULL,
	"type" TEXT NOT NULL,
	CONSTRAINT "type_of_classes_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "positions_of_teacher" (
	"id" serial NOT NULL,
	"position" TEXT,
	"briefly" TEXT,
	CONSTRAINT "positions_of_teacher_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "courses" (
	"id" serial NOT NULL,
	"course" TEXT NOT NULL,
	CONSTRAINT "course_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);



CREATE TABLE "subgroups" (
	"id" serial NOT NULL,
	"subgroup" TEXT NOT NULL,
	CONSTRAINT "subgroups_pk" PRIMARY KEY ("id")
) WITH (
  OIDS=FALSE
);




ALTER TABLE "shedule" ADD CONSTRAINT "shedule_fk0" FOREIGN KEY ("audience") REFERENCES "audiences"("id");
ALTER TABLE "shedule" ADD CONSTRAINT "shedule_fk1" FOREIGN KEY ("class") REFERENCES "classes"("id");
ALTER TABLE "shedule" ADD CONSTRAINT "shedule_fk2" FOREIGN KEY ("day") REFERENCES "days"("id");
ALTER TABLE "shedule" ADD CONSTRAINT "shedule_fk3" FOREIGN KEY ("faculty") REFERENCES "facultys"("id");
ALTER TABLE "shedule" ADD CONSTRAINT "shedule_fk4" FOREIGN KEY ("group_") REFERENCES "groups_"("id");
ALTER TABLE "shedule" ADD CONSTRAINT "shedule_fk5" FOREIGN KEY ("subject") REFERENCES "subjects"("id");
ALTER TABLE "shedule" ADD CONSTRAINT "shedule_fk6" FOREIGN KEY ("teacher") REFERENCES "teachers"("id");
ALTER TABLE "shedule" ADD CONSTRAINT "shedule_fk7" FOREIGN KEY ("type_of_class") REFERENCES "type_of_classes"("id");
ALTER TABLE "shedule" ADD CONSTRAINT "shedule_fk8" FOREIGN KEY ("week") REFERENCES "weeks"("id");
ALTER TABLE "shedule" ADD CONSTRAINT "shedule_fk9" FOREIGN KEY ("subgroup") REFERENCES "subgroups"("id");




ALTER TABLE "teachers" ADD CONSTRAINT "teachers_fk0" FOREIGN KEY ("position") REFERENCES "positions_of_teacher"("id");

ALTER TABLE "groups_" ADD CONSTRAINT "groups__fk0" FOREIGN KEY ("course") REFERENCES "courses"("id");

ALTER TABLE "groups_" ADD CONSTRAINT "groups__fk1" FOREIGN KEY ("faculty") REFERENCES "facultys"("id");