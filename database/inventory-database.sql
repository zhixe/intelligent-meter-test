CREATE FUNCTION generate_tracking_id(t text, id bigint)
returns text
as
$$
  SELECT t || TO_CHAR(id,'FM000000000');
$$
language sql
immutable;

CREATE SEQUENCE event_seq;

CREATE TABLE "employees" (
    "employee_id" text,
    "username" text UNIQUE,
    "password" text NOT NULL,
    "email" text UNIQUE,
    "first_name" text NOT NULL,
    "last_name" text,
    "department" text,
    "position" text,
    "employment_type" text NOT NULL,
    PRIMARY KEY ("employee_id")
);

CREATE TABLE "meters" (
    "meter_serial" text,
    "manufacturer" text NOT NULL,
    "store_region" text NOT NULL,
    "size" smallint,
    "type" text,
    "model" text,
    PRIMARY KEY ("meter_serial")
);

CREATE TABLE "tracking" (
    "event_id" bigint NOT NULL DEFAULT NEXTVAL ('event_seq'),
    "employee_id" text,
    "meter_serial" text,
    "event_type" char(3) NOT NULL,
    "tracking_id" text GENERATED ALWAYS AS (generate_tracking_id(event_type, event_id)) STORED,
    "timestamp" timestamp,
    "source" text,
    "destination" text,
    "status" text,
    PRIMARY KEY ("event_id"),
    CONSTRAINT "FK_tracking.meter_serial"
        FOREIGN KEY ("meter_serial")
        REFERENCES "meters"("meter_serial"),
    CONSTRAINT "FK_tracking.employee_id"
        FOREIGN KEY ("employee_id")
        REFERENCES "employees"("employee_id")
);

CREATE TABLE "customers" (
    "customer_id" text,
    "username" text UNIQUE,
    "password" text,
    "email" text UNIQUE,
    "first_name" text NOT NULL,
    "last_name" text,
    "address" text,
    "ic_no" text UNIQUE,
    "phone_no" text,
    "age" smallint,
    PRIMARY KEY ("customer_id")
);

CREATE TABLE "installations" (
    "installation_id" text,
    "meter_serial" text,
    "customer_id" text,
    "employee_id" text,
    "installation_date" timestamp,
    "status" bool,
    PRIMARY KEY ("installation_id"),
    CONSTRAINT "FK_installations.employee_id"
        FOREIGN KEY ("employee_id")
        REFERENCES "employees"("employee_id"),
    CONSTRAINT "FK_installations.customer_id"
        FOREIGN KEY ("customer_id")
        REFERENCES "customers"("customer_id"),
    CONSTRAINT "FK_installations.meter_serial"
        FOREIGN KEY ("meter_serial")
        REFERENCES "meters"("meter_serial")
);

--for testing
/*
INSERT INTO tracking (event_type) VALUES ('TRA');
INSERT INTO tracking (event_type) VALUES ('INS');
*/