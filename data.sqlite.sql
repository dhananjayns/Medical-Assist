BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "alembic_version" (
	"version_num"	VARCHAR(32) NOT NULL,
	CONSTRAINT "alembic_version_pkc" PRIMARY KEY("version_num")
);
CREATE TABLE IF NOT EXISTS "Disease" (
	"id"	INTEGER NOT NULL,
	"disease_name"	VARCHAR(64) NOT NULL,
	"prevention"	VARCHAR NOT NULL,
	"cause"	VARCHAR,
	"cure"	VARCHAR,
	"doc_type"	VARCHAR NOT NULL,
	"age_group"	INTEGER NOT NULL,
	UNIQUE("disease_name"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "Doctors" (
	"id"	INTEGER NOT NULL,
	"doc_name"	VARCHAR NOT NULL,
	"doc_type"	VARCHAR NOT NULL,
	"doc_location"	VARCHAR NOT NULL,
	"doc_hospital"	VARCHAR,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "reviews" (
	"id"	INTEGER NOT NULL,
	"doc_name"	VARCHAR,
	"username"	VARCHAR,
	"rating"	INTEGER,
	"doc_review"	VARCHAR,
	"date"	DATETIME,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER NOT NULL,
	"email"	VARCHAR(64) NOT NULL,
	"username"	VARCHAR(64) NOT NULL,
	"password_hash"	VARCHAR(128),
	"location"	VARCHAR(64),
	UNIQUE("username"),
	UNIQUE("email"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "symptoms" (
	"disease_id"	INTEGER NOT NULL,
	"symptom_name"	VARCHAR NOT NULL,
	PRIMARY KEY("disease_id","symptom_name")
);
INSERT INTO "alembic_version" ("version_num") VALUES ('112dc4244688');
INSERT INTO "Disease" ("id","disease_name","prevention","cause","cure","doc_type","age_group") VALUES (1,'Cold','Wash your hands—especially before eating and preparing food, after using the bathroom, after wiping your nose, and after coming in contact with someone who has a cold,Avoid touching your eyes and nose to prevent the spread of viruses from your hands,Avoid contact with those who have a cold.','Although many types of viruses can cause a common cold, rhinoviruses are the most common culprit. A cold virus enters your body through your mouth, eyes or nose. The virus can spread through droplets in the air when someone who is sick coughs, sneezes or talks','Drink Plenty of fluids,preferably Hot Water with Turmeric','Physician','Common'),
 (2,'Fever','Most fevers are caused by infection. Avoiding sources of infection and maintaining good hygiene practices are the best way to prevent a fever. ... Proper hygiene: Wash hands frequently. Avoid contact with sick people','an infection, such as strep throat, flu, chickenpox, or pneumonia','Taking Antibioitics','Physician','Common'),
 (3,'Dengue','As a mosquito-borne disease, preventing dengue is as simple as preventing mosquito bites','Dengue fever is caused by any one of four types of dengue viruses spread by mosquitoes that thrive in and near human lodgings. When a mosquito bites a person infected with a dengue virus, the virus enters the mosquito. When the infected mosquito then bites another person, the virus enters that person''s bloodstream','Tylenol Vaccine ,Aspirine','Physician','Common'),
 (4,'Chicken Pox','The best way to prevent chickenpox is to get the chickenpox vaccine','Chickenpox is caused by the varicella-zoster virus, which also causes shingles. Chickenpox is highly contagious and spreads by closeness and contact with someone with chickenpox','Cool compresses applied to blisters may give relief,You can give cool-water baths every three to four hours, adding baking soda to the water to calm itching,Trimming fingernails,There is no specific cure.It will resolve within a week without treatment','Pediatrician','Children'),
 (5,'Arthritis','You can''t always prevent arthritis.But Eat fish. Certain fish are rich in omega-3 fatty acids, a healthy polyunsaturated fat','abnormal metabolism, leading to gout and pseudogout,infections, such as in the arthritis of Lyme disease,immune system dysfunction','Nonsteroidal anti-inflammatory drugs (NSAIDs). NSAIDs reduce both pain and inflammation,Joint Replacement Surgery,Physical Therapy','Orthopedic','Above 50'),
 (6,'Obsessive Compulsive Disorder','There''s no sure way to prevent obsessive-compulsive disorder. However, getting treatment as soon as possible may help prevent OCD from worsening and disrupting activities and your daily routine','Imbalance in Neurotransmitter','As with all forms of mental illness, there is no known OCD cure.
However Cognitive Behavioural Therapy helps','Psychiatrist','20-50'),
 (7,'Cataract','Quit Smoking if You are an addict .Sun Glasses Recommended','Aging,Diabetes','Replacing Natural Eyelens with Introcular Lens','ENT','Above 50'),
 (8,'Mumps','The MMR vaccine protects against mumps. The measles, mumps, and rubella (MMR) vaccine can help prevent the disease. ... Two doses of MMR are 88 percent effective, and one dose is 78 percent effective','The Virus. Mumps is a viral illness caused by a paramyxovirus, a member of the Rubulavirus family. The average incubation period for mumps is 16 to 18 days, with a range of 12 to 25 days','There is no cure, but the patient should rest and drink plenty of fluids, especially water. To reduce the symptoms of pain and fever, an over-the-counter anti-inflammatory may be recommended such as ibuprofen. Home remedies for mumps include: a warm or cold compress to ease pain and tenderness','Pediatrician','Children'),
 (9,'STDs','Use latex condoms every time you have sex,Avoid sharing towels or underclothing,Needles,Get a vaccination for hepatitis B','Unprotected Intercourse with Infected people','Antibiotics. Antibiotics, often in a single dose, can cure many sexually transmitted bacterial and parasitic infections, including gonorrhea, syphilis, chlamydia and trichomoniasis,Antiviral drugs. If you have herpes or HIV ','Psychiatrist','Common'),
 (10,'Anxiety Disorders (including Panic Attacks and Phobias)','Prevention of everyday anxiety essentially involves an awareness of life''s stresses and your own ability to cope with them,Meditation and Yoga and Exercises','Stress and Tensions','Awareness of life''s stresses ,Meditation and Yoga and Exercises','Psychiatrist','20-50');
INSERT INTO "Doctors" ("id","doc_name","doc_type","doc_location","doc_hospital") VALUES (1,'NandaKumar ','Physician','Hebbal','Columbia Asia '),
 (2,'Meena ','Psychiatrist','Hebbal','Columbia Asia '),
 (3,'Santosh','ENT','Hebbal','Columbia Asia '),
 (4,'Naveen Chand','Orthopedic','Hebbal','Aster CMI Hospital'),
 (5,'Manas','Pediatrician','Hebbal','Little Star Children Clinic'),
 (6,'Jayram','Pediatrician','J P Nagar','Apollo Clinic'),
 (7,'VenuGopal','Orthopedic','J P Nagar','Apollo Clinic'),
 (8,'Harsha','Physician','J P Nagar','Apollo Clinic'),
 (9,'Prerana','ENT','J P Nagar','Prerana Clinic'),
 (10,'M J Thomas','Psychiatrist','J P Nagar','Sagar Hospital'),
 (11,'GiriRaj','Orthopedic','Shivaji Nagar','Hosmat Hospital'),
 (12,'B V Balachandra','Pediatrician','Shivaji Nagar','Manipal Hospital'),
 (13,'Narvir','Physician','Shivaji Nagar','Doshi Clinic'),
 (14,'Noor Shabana','ENT','Shivaji Nagar','Hiba ENT Care '),
 (15,'Soumya Hegde','Psychiatrist','Shivaji Nagar','Anna Swamy Mudaliar Hospital '),
 (16,'Praveen Kumar','ENT','Wilson Garden','Agadi Hospital'),
 (17,'K Praveen ','Psychiatrist','Wilson Garden','Agadi Hospital'),
 (18,'Anand','Orthopedic','Wilson Garden','Gleneagles Global Hospital'),
 (19,'A Jagadeesh','Pediatrician','Wilson Garden','Abhaya Hospital'),
 (20,'P Jayraj','Physician','Wilson Garden','Raju Clinic'),
 (21,'Kalpana','Pediatrician','Kengeri','Siri Clinic'),
 (22,'Ivan Mani','ENT','Kengeri','Siri Clinic'),
 (23,'Kishore','Orthopedic','Kengeri','Mathru Orthopedic Hospital'),
 (24,'Karthik K N','Psychiatrist','Kengeri','Infinity Sexual Heath Center'),
 (25,'T Surendra Reddy','Physician','Kengeri','B G S Global Hospital ');
INSERT INTO "reviews" ("id","doc_name","username","rating","doc_review","date") VALUES (1,'NandaKumar ','dhananjayns',5,'hello','2019-11-09 15:20:13.677003'),
 (2,'T Surendra Reddy','dhanushbp',4,'good','2019-11-10 00:06:21.054496'),
 (5,'P Jayraj','example',4,'Very welcoming Doctor','2019-11-17 10:18:33.399410'),
 (6,'T Surendra Reddy','dhanushbp',2,'sd','2019-11-25 21:11:01.141450');
INSERT INTO "users" ("id","email","username","password_hash","location") VALUES (1,'dhananjay.sabhahit@gmail.com','dhananjayns','pbkdf2:sha256:50000$1tVlNdFR$c486012c396f96b5d2db3af1c22b5d93b9d321ec19b3b6cb68a113c20c2e9f09','Hebbal'),
 (3,'dhanu.sabhahit@gmail.com','dhananjay','pbkdf2:sha256:50000$VgNHNJVO$f3b7904a01c756adc3497571fe858afef848a299845a3f8dbbbb4a127670d454','Wilson Garden'),
 (4,'akhileshudayashankar@gmail.com','Akhilesh','pbkdf2:sha256:50000$i7LwFfOc$320ac47c1600c99af59a06e86b9b4e8f4b3cfcc6c5ce231cb4312597e4391676','Shivaji Nagar'),
 (6,'example@example.example','example','pbkdf2:sha256:50000$2sSsfPSt$8cebe548b0f8cb0bf990fa9e2d661a5fdfbed843a59cdd8a5c3e128f6842f17c','Wilson Garden'),
 (7,'dhanusabhahit@gmail.com','dhanu','pbkdf2:sha256:50000$eJDZXevL$93d0c26ba1190f1b08f6fef6a648c3acb3181a0fd545163327ce7cc1b49330c1','J P Nagar'),
 (8,'admin@medassist.com','Admin','pbkdf2:sha256:50000$H58Ko2rA$21e62ea455fb0cbd34f295f6b0c04de3527549737b994ec1a4688fb8b180eb24','J P Nagar'),
 (9,'dhanushbp.cs17@rvce.edu.in','dhanushbp','pbkdf2:sha256:50000$5dmg03QJ$d98b29702e1818b9f248326fc20a15f5fa8e29ea5c1053318f47af2cfefb6979','Kengeri');
INSERT INTO "symptoms" ("disease_id","symptom_name") VALUES (1,'Runny or stuffy nose'),
 (1,'Sore throat'),
 (1,'Congestion
'),
 (1,'Sneezing'),
 (1,'A mild headache and Slight body aches'),
 (1,'Watery Eyes
'),
 (2,'Skin flushing or hot skin'),
 (2,'Rapid heart rate and/or palpitations
'),
 (2,'Excessive sweating and Aching muscles'),
 (2,'Shivering, shaking, and chills'),
 (2,'Temperature greater than 100.4 F
'),
 (3,'Sudden, high fever and Severe abdominal pain'),
 (3,'Severe headaches,Bleeding from your gums or nose'),
 (3,'Skin rash, which appears two to five days after the onset of fever'),
 (3,'Nausea or Vomiting and Fatigue'),
 (3,'Pain behind the eyes');
COMMIT;
