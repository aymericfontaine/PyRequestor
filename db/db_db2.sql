CREATE TABLE REQUEST	
(	
	ID INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
	NUM INTEGER NOT NULL UNIQUE,
	LABEL CHAR(100) NOT NULL,
	REQ VARCHAR(5000) NOT NULL,

	PRIMARY KEY(ID)
);


CREATE TABLE REQUEST_PARAM	
(	
	ID INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
	IDREQUEST INTEGER NOT NULL,
	NUM INTEGER NOT NULL,
	LABEL CHAR(50) NOT NULL,
	HELP VARCHAR(50),

	PRIMARY KEY(ID),
	FOREIGN KEY (IDREQUEST) REFERENCES REQUEST (ID),
	UNIQUE (IDREQUEST, NUM)
);



INSERT INTO REQUEST (NUM, LABEL, REQ)
VALUES (
	10000,
	'Users',
	'SELECT * FROM IPTW2FBIG.EXAMPLE_USER'
);



INSERT INTO REQUEST (NUM, LABEL, REQ)
VALUES (
	20000,
	'Users by last name',
	'SELECT * FROM IPTW2FBIG.EXAMPLE_USER WHERE UPPER(LASTNAME) = UPPER(''{0}'')'
);

INSERT INTO REQUEST_PARAM (IDREQUEST, NUM, LABEL, HELP)
VALUES ((SELECT MAX(ID) FROM REQUEST), 1, 'LASTNAME', 'XXXXXXXXXX');



-- EXAMPLE
CREATE TABLE EXAMPLE_USER	
(	
	ID INTEGER NOT NULL GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
	LASTNAME VARCHAR(50),
	FIRSTNAME VARCHAR(50),
	CITY VARCHAR(30),
	
	PRIMARY KEY(ID)
);

INSERT INTO EXAMPLE_USER (LASTNAME, FIRSTNAME, CITY)
VALUES ('SMITH', 'JOHN', 'NEW YORK');

INSERT INTO EXAMPLE_USER (LASTNAME, FIRSTNAME, CITY)
VALUES ('SMITH', 'CHARLES', 'NEW YORK');

INSERT INTO EXAMPLE_USER (LASTNAME, FIRSTNAME, CITY)
VALUES ('FAVE', 'ESTEBAN', 'PARIS');

INSERT INTO EXAMPLE_USER (LASTNAME, FIRSTNAME, CITY)
VALUES ('TRIUMPH', 'LUCIE', 'LONDON');