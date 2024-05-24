CREATE TABLE "Login_credentials" (
    "username" VARCHAR(20),
    "password" VARCHAR(50) NOT NULL,
    "login_attempt" SMALLINT,
    "last_login" TIMESTAMP,
    PRIMARY KEY ("username")
);

CREATE TABLE "Employees" (
    "employee_id" VARCHAR(20),
    "username" VARCHAR(20) UNIQUE,
    "employee_email" VARCHAR(50) UNIQUE,
    "first_name" VARCHAR(100) NOT NULL,
    "last_name" VARCHAR(100),
    "department" VARCHAR(20),
    "position" VARCHAR(20),
    "employment_type" VARCHAR(20) NOT NULL,
    PRIMARY KEY ("employee_id"),
    CONSTRAINT "FK_Employees.username"
        FOREIGN KEY ("username")
        REFERENCES "Login_credentials"("username")
);

CREATE TABLE "meters" (
    "meter_serial" TEXT,
    "meter_manufacturer" VARCHAR(50) NOT NULL,
    "store_region" VARCHAR(50) NOT NULL,
    "meter_size" SMALLINT,
    "meter_type" VARCHAR(50),
    "meter_model" VARCHAR(50),
    PRIMARY KEY ("meter_serial")
);

CREATE TABLE "Tracking" (
    "tracking_id" VARCHAR(20),
    "user_id" VARCHAR(20),
    "meter_serial" VARCHAR(20),
    "source" VARCHAR(20),
    "destination_address" VARCHAR(20) NOT NULL,
    "status" bool,
    PRIMARY KEY ("tracking_id"),
    CONSTRAINT "FK_Tracking.meter_serial"
        FOREIGN KEY ("meter_serial")
        REFERENCES "Meters"("meter_serial"),
    CONSTRAINT "FK_Tracking.user_id"
        FOREIGN KEY ("user_id")
        REFERENCES "Employees"("employee_id")
);

CREATE TABLE "Customers" (
    "customer_id" VARCHAR(20),
    "meter_serial" VARCHAR(20),
    "username" VARCHAR(20) UNIQUE,
    "customer_email" VARCHAR(50) UNIQUE,
    "first_name" VARCHAR(100) NOT NULL,
    "last_name" VARCHAR(100),
    "address" VARCHAR(300),
    "ic_no" CHAR(12) UNIQUE,
    "phone_no" VARCHAR(20),
    "age" SMALLINT,
    PRIMARY KEY ("customer_id"),
    CONSTRAINT "FK_Customers.meter_serial"
        FOREIGN KEY ("meter_serial")
        REFERENCES "Meters"("meter_serial"),
    CONSTRAINT "FK_Customers.username"
        FOREIGN KEY ("username")
        REFERENCES "Login_credentials"("username")
);

CREATE TABLE "Installations" (
    "installations_id" VARCHAR(20),
    "customer_id" VARCHAR(20),
    "meter_serial" VARCHAR(20),
    "user_id" VARCHAR(20),
    "installation_date" DATE,
    "status" bool,
    PRIMARY KEY ("installations_id"),
    CONSTRAINT "FK_Installations.user_id"
        FOREIGN KEY ("user_id")
        REFERENCES "Employees"("employee_id"),
    CONSTRAINT "FK_Installations.meter_serial"
        FOREIGN KEY ("meter_serial")
        REFERENCES "Meters"("meter_serial"),
    CONSTRAINT "FK_Installations.customer_id"
        FOREIGN KEY ("customer_id")
        REFERENCES "Customers"("customer_id")
);



