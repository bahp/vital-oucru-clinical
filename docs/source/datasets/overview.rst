The OUCRU datasets
==================

This repository contains an aggregation of datasets collected from prospective
clinical studies conducted by the Oxford University Clinical Research Unit (OUCRU)
between 2009 and 2021. All these studies have been conducted in healthcare facilities
within the Hospital for Tropical Diseases (HTD) in Ho Chi Minh City, Vietnam.

| Data collection: ``Oxford University Clinical Research Unit``
| Data cleaning: ``Imperial College London``
| Repository setup: ``Imperial College London``


.. todo::
    List of things:

        - Improve introduction, mention vital consortium (url)
        - [Auto-generate table with brief summary of datasets]
        - [Include links to manuscripts and other resources] - done

.. table:: Overview of clinical study aims
    :widths: 6 8 60 10

    ======= ========= ================================================= ========
    Name    Period     Aim                                              Patients
    ======= ========= ================================================= ========
    df      1999-2009 Describe clinical features of ``DSS`` in children 1719
    md      2001-2009 Describe clinical features of ``NSD`` in children 3044
    dr      2005-2008 Describe clinical features of ``NSD`` in children 1542
    fl      xxxx-xxxx -                                                 -
    06dx    2009-2011 Effect of steroid in Dengue                       330
    13dx    2010-2014 Diagnostic accuracy of NS1                        8108
    32dx    2013-2016 Intravascular volume assessment (CRI)             75
    42dx    2017-2018 Clinical features of DSS in pregnant women?       664
    d001    2011      -                                                 112
    01nva   2020-2021 Clinical features of Dengue patients (wearables)  155
    ======= ========= ================================================= ========


``DSS`` - Dengue Shock Syndrome | ``NSD`` - Non Severe Dengue | ``CRI`` -


The table below includes the manuscripts that have been published along the
years using the data collected in at least one of the previously described
studies. The columns describe the dataset used (name), the title of the
manuscript, the year in which it was published and a reference to the full
manuscript for download as pdf.

.. list-table:: Published manuscripts
   :widths: 6 50 10 10
   :header-rows: 1

   * - Data
     - Title
     - Year
     - Ref
   * - df
     - Comparison of three fluid solutions for resucitation in DSS
     - 2005
     - |pdf-wills2005|
   * - df
     - Clinical characteristics of dengue shock syndrome in vietnamese children
     - 2013
     - |pdf-lam2013|
   * - df
     - A prognostic model for development of profound shock in DSS
     - 2015
     - |pdf-lam2015|
   * - md
     - The value of daily platelet counts for predicting DSS
     - 2017
     - |pdf-lam2017|
   * - dr
     - Assessment of microalbuminuria for early diagnosis and risk prediction
     - 2013
     - |pdf-tien2013|
   * - 06dx
     - Effects of short-course oral corticosteroid therapy in early dengue infection
     - 2012
     - |pdf-tam2012|
   * - 06dx
     - Corticosteroids for Dengue - Why don't they work?
     - 2013
     - |pdf-nguyen2013|
   * -
     - Clinical features of Dengue in a large vietnamese cohort
     - 2012
     - |pdf-the2012|
   * - 13dx
     - Sensitivity and specificity of a novel classifier for the early diagnosis
     - 2015
     - |pdf-tuan2015|
   * - 13dx
     - An evidence-based algorithm for early prognosis of severe dengue
     - 2017
     - |pdf-nguyen2017|
   * - 32dx
     - Microvascular and endothelial function for risk prediction in dengue
     - 2012
     - |pdf-yacoub2015|
   * - 32dx
     - Association of microvascular function and endothelial biomarkers ...
     - 2016
     - |pdf-yacoub2016|
   * - 32dx
     - Cardio-haemodynamic assessment and venous lactate in severe dengue ...
     - 2017
     - |pdf-yacoub2017|

********
Overview
********

This is an overview of the overall dataset which is a compendium of all the data
collected during the previously mentioned studies. [complete]

.. todo::

    List of things:

        - Write introduction
        - Explain dsource
        - Explain study_no
        - Explain date
        - Briefly mention DataBlend


Description of features
-----------------------

The list of features available in the aggregated dataset is included in the
table below. Please note that some features might not be available across
all datasets yet that information will be provided in subsequent sections.

The following table includes:

  - **name:** the name of the feature
  - **dtype:** the data type of the feature
  - **unit:** the unit of the feature (if applicable)
  - **code:** the code of the feature (if applicable)
  - **ctype:** the class type of the feature
  - **description:**: brief description of the feature
  - **categories**: The list of allowed categories
  - **unique**: The unique values found in the data
  - **corrections**: The corrections [pending...]
  - **ranges**: Useful reference ranges [pending...]


.. |br| raw:: html

    <br/>

.. note::
    Remember you can:

         - ``reorder`` by any column.
         - ``search`` using the searchbox to filter by any column. This box allows
            you to search by the name of the feature (e.g. bleeding will show all
            features including bleeding) but in addition it will return any feature
            that contains such word in its description. For instance, you can use
            it to find skin, lung, chest, blood/bleeding related features.
         - ``explore`` more information through the + dropdown.
         - ``export`` the table to any of the available formats.

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_combined.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>


Presence of features in datasets
--------------------------------

As we have mentioned below, not all the features are available accross
the studies. To provide more specific information, the table below displays
the number of rows containing a value different from None for each feature
an the corresponding study. At the end of the table a variable denoted
``n_sets`` indicate the number of datasets in which the variable is present.

.. note:: The table has been automatically generated from
          the combined dataset in ``tidy`` structure. Thus,
          each row contains the features recorded for a
          single patient on a given day.

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_count.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>


Profiles table
--------------

For more information on each of the datasets, please visit the links below.

.. warning:: Some of the links might not work because files are too long
             to be uploaded to standard git. To solve this issue use
             git-large-files.

.. list-table:: Links to detailed information for each dataset
   :widths: 6 10 10
   :header-rows: 1

   * - Name
     - ``dataprep``
     - ``pandas-profile``
   * - df
     -
        .. raw:: html

           <a href="../_static/datasets/profile-dataprep/df_data_tidy_corrected.html"
              target="_blank"> Link </a>
     -
        .. raw:: html

           <a href="../_static/datasets/profile-pandas/df_data_tidy_corrected.html"
              target="_blank"> Link </a>

   * - md
     -
        .. raw:: html

           <a href="../_static/datasets/profile-dataprep/md_data_tidy_corrected.html"
              target="_blank"> Link </a>
     -
        .. raw:: html

           <a href="../_static/datasets/profile-pandas/md_data_tidy_corrected.html"
              target="_blank"> Link </a>
   * - dr
     -
        .. raw:: html

           <a href="../_static/datasets/profile-dataprep/dr_data_tidy_corrected.html"
              target="_blank"> Link </a>
     -
        .. raw:: html

           <a href="../_static/datasets/profile-pandas/dr_data_tidy_corrected.html"
              target="_blank"> Link </a>
   * - 06dx
     -
        .. raw:: html

           <a href="../_static/datasets/profile-dataprep/06dx_data_tidy_corrected.html"
              target="_blank"> Link </a>
     -
        .. raw:: html

           <a href="../_static/datasets/profile-pandas/06dx_data_tidy_corrected.html"
              target="_blank"> Link </a>
   * - 13dx
     -
        .. raw:: html

           <a href="../_static/datasets/profile-dataprep/13dx_data_tidy_corrected.html"
              target="_blank"> Link </a>
     -
        .. raw:: html

           <a href="../_static/datasets/profile-pandas/13dx_data_tidy_corrected.html"
              target="_blank"> Link </a>
   * - 32dx
     -
        .. raw:: html

           <a href="../_static/datasets/profile-dataprep/32dx_data_tidy_corrected.html"
              target="_blank"> Link </a>
     -
        .. raw:: html

           <a href="../_static/datasets/profile-pandas/32dx_data_tidy_corrected.html"
              target="_blank"> Link </a>
   * - 42dx
     -
        .. raw:: html

           <a href="../_static/datasets/profile-dataprep/42dx_data_tidy_corrected.html"
              target="_blank"> Link </a>
     -
        .. raw:: html

           <a href="../_static/datasets/profile-pandas/42dx_data_tidy_corrected.html"
              target="_blank"> Link </a>
   * - d001
     -
        .. raw:: html

           <a href="../_static/datasets/profile-dataprep/d001_data_tidy_corrected.html"
              target="_blank"> Link </a>
     -
        .. raw:: html

           <a href="../_static/datasets/profile-pandas/d001_data_tidy_corrected.html"
              target="_blank"> Link </a>
   * - 0n1nva
     -
        .. raw:: html

           <a href="../_static/datasets/profile-dataprep/01nva_data_tidy_corrected.html"
              target="_blank"> Link </a>
     -
        .. raw:: html

           <a href="../_static/datasets/profile-pandas/01nva_data_tidy_corrected.html"
              target="_blank"> Link </a>

****************
List of datasets
****************

The df dataset
--------------

.. warning:: Important things to consider...

The trial was a ``single-center``, ``randomized``, ``doubleblind`` comparison of an isotonic crystalloid solution
(Ringer’s lactate) and two isotonic colloid solutions (6% dextran 70 [dextran] and 6%
hydroxyethyl starch 200/0.5 [starch]) for emergency resuscitation of ``children`` with ``dengue shock syndrome``.
The children were stratified according to pulse pressure at admission, a marker of the severity of the
vascular leak. No children in the group with severe shock received a crystalloid because of concerns
about the potential development of critical fluid overload without access to advanced respiratory support.
The study took place in the pediatric intensive care unit at the Hospital for Tropical Diseases in Ho
Chi Minh City, Vietnam. The ethics and science committee of the hospital approved the protocol.

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_df.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>


.. warning:: The excel worksheet ``DF`` (???) ...

    - Need to clarify when things happend, there are various dates (admission, enrolment)
      etc and all the features are collected here. Need to know what date is associated
      to each feature.

    - Needs reviewing

    - What is hemo, hemo2
    - What is D1, d2.

    - new_xxxx but stil with date_admission date... shame.
    - no follow up date.

The fl dataset
--------------


.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_fl.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>


.. warning:: The excel worksheet ``FL_CLINICAL_SUM` (PCR):

      - It has vomit his, vomit exam and vomit. should they be assigned
        to date_onset, date_admission and date_enrolment? swap enrolment
        and admission?

      - Needs to be revisited

- Not finished!

The md dataset
--------------

.. warning:: Important things to consider...

            - Does it include multiple shock information.
            - No PCR date available?
            - ETC

A ``prospective observational study`` of ``children`` hospitalized with ``suspected dengue`` at the HTD
in Ho Chi Minh City, Viet Nam, was conducted between 2001 and 2009. The cohort included
any child aged between 5 and 15 years admitted to the paediatric dengue ward at HTD with
clinically suspected dengue, whose parent/guardian gave written informed consent for them to
be enrolled in the study following detailed explanation by a trained study doctor. Consecutive
suspected dengue cases identified during the morning ward round were approached by study
staff as potential participants; commencing on Monday morning the process continued until
up to 10 suspected dengue cases had been enrolled for that week. Of note, the paediatric dengue
ward is responsible for managing children with uncomplicated illness only, and HTD
policy dictates that any child who develops DSS or about whom there is concern (typically
development of warning signs necessitating monitoring more frequently than 4–6 hourly) is
transferred to the Paediatric Intensive Care Unit (PICU). During the study period all children
admitted to PICU with DSS were recruited into a concurrent pediatric cohort

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_md.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>

.. warning:: The excel worksheet ``MD_lab`` (laboratory):

      - What is from_adm? probably day_from_admission?

.. warning:: The excel worksheet ``MD_clinical`` (clinical):

      - day_ill with respect to date_admission? date_enrolment? date_fever?

      - bleeding contains categories (No, skin only and mucosal) wich have
        just been converted to booleans. However, not sure what date to
        use. Since it is a compound we are not retrieving it as we have
        the subcategories (Skin, mucosal).

      - what is d2shock?

      - Do the variables sigbled, sigbled_s, bleed_hos, overload refer to the admission or to the discharge?

.. warning:: The excel worksheet ``MD_PCR` (PCR):

      - Only extracting the summart columns serotype and viremia.

.. warning:: The excel worksheet ``MD_Tien_hist` :

      - Ignore, such data looks like it is already in the second sheet (CLINICAL).

.. warning:: The excel worksheet ``MD_Tien_exam` :

      - Ignore, such data looks like it is already in the second sheet (CLINICAL).

.. warning:: The excel worksheet ``MD_Tien_DRvalue` :

      - Ignore, such data looks like it is already in the PCR sheet.
      - It has (6100 rows!, while clinical only 3000)
      - IT is missing a day.

.. warning:: The excel worksheet ``MD_Tien_invest` :

      - Ignore, such data looks like it is already in the second sheet (CLINICAL).
      - It has 3400 rows while clinical has 3020 aprox)

The dr dataset
--------------

We conducted a ``prospective descriptive`` study of ``febrile
children``, aged 5–15 years, attending two ``primary`` health care
clinics in Ho Chi Minh City, Vietnam. Clinic A is a single-handed
practice run by a senior paediatrician, while Clinic B is the walk-in
paediatric clinic at District 8 Hospital. This study forms one part of
a large community study on dengue, the clinical aspects of which
have been described previously, but briefly all children presenting
with fever and clinically suspected dengue to either clinic were
eligible for enrolment following written informed consent [14].
Recruitment was targeted towards patients presenting during the
early febrile period, ideally within the first 72 hours from fever
onset, although patients presenting up to 96 hours from fever onset
could be enrolled. Patients were seen daily until afebrile for two
consecutive days, with detailed clinical information recorded in a
standard format and a 1 ml EDTA blood sample obtained for
clinical (haematocrit estimation and platelet count) and diagnostic
purposes, together with a random urine sample. Clinic physicians
were responsible for all management decisions; if hospitalization
was considered necessary the children were admitted to HTD and
the daily assessments continued, following the same protocol as the
outpatient subjects. Patients were invited to attend for review 2–4
weeks from illness onset.

Illness day 1 was defined as the day of reported fever onset.
Defervescence day was defined as the first day with no history of
fever since the previous day’s visit and with a measured
temperature #37.5uC in the clinic. The following outcomes were
summarised from the daily assessments: the platelet nadir between
days 3–8 of illness; the presence or absence of skin and/or mucosal
bleeding; the percentage hemoconcentration, defined as the
percentage increase in haematocrit comparing the maximum
value recorded between days 3–8 of illness, to a baseline value
taken as the lowest result obtained on or before illness day 2 or
after day 14, or a local population value matched for age and sex if
no individual baseline was available [14].

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_dr.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>

.. warning:: The excel worksheet ``DR1_2232_ENROL` (PCR):

      - Needs reviewing.

.. warning:: The excel worksheet ``NEGATIVE_LIST_STUDY` (PCR):

      - The day of ilness not clear whether to assign to date_fu or date_fever

The d001 dataset
----------------

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_d001.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>


.. warning:: The excel worksheet ``D001_CLINICAL` (PCR):

      - The day of ilness not clear whether to assign to date_admission or date_enrolment
      - No categories specified for outcome 1, 2, 3, 4

.. warning:: The excel worksheet ``D001_LAB` (PCR):
       - Is the inmue status related with the serology secondary thus meaning that had
         dengue before?

.. warning:: The excel worksheet ``D001_SERO_DATA` (PCR):
       - Probably needs reviewing. Only basic extracted.
       - It has bad dates because times given by day of illness and no reference date.


.. warning:: The excel worksheet ``D001_SERO_DATA_INMUNE` (PCR):
       - Probably needs reviewing. Only basic extracted.
       - It has bad dates because times given by day of illness and no reference date.

.. warning:: The excel worksheet ``D001_SERO_DEMO` (PCR):
       - Repeated from first sheet.


The 06dx dataset
----------------

We performed a randomized, placebo-controlled, partially blinded trial of early corticosteroid
therapy in Vietnamese children and young adults with suspected dengue virus infection. The study
took place on designated infectious diseases wards at the Hospital for Tropical Diseases of Ho
Chi Minh City, with approval from the Ethical Committee of the Ministry of Health of Vietnam and
the Oxford Tropical Research Ethics Committee.


.. note::

  - Bleeding severity (1 - only skin, 2 mild mucosal +/- skin and 3 severe either mucosal or skin)

.. warning::

   - What does ``SCR`` stand for?

   - In ``HIST`` (history) ...

      - One date has a bad time format (24:00 should be 00:00).
      - The date of fever has been used for all the history symptoms.


.. warning:: The excel worksheet ``SCR`` (???) ...

      - Has ``Pregnant`` and ``PregnancyPos``. All the values for both are 2,
        which assume is False (based on other datasets). However, it has been
        collected that they might actually represent only those who were
        pregnant?

.. warning:: The excel worksheet ``HIST`` (History) ...

      - Has ``Dayillness``. Should this be matche with date_admission or
        date_enrolment to get the date of onset of symptoms?

      - Has ``HeartSound`` with all values as 1. Then because the variable
        ``HeartSoundDesc`` is all blank, a value of 1 in HeartSound means
        that the heart sound was normal (heart_sound_abnormal; 1:False, 2:True).

      - Has ``CNS`` with all values as 1. Then because the variable
        ``CNSDesc`` is all blank, a value of 1 in CNS means
        that the CNS was normal (cns_abnormal; 1:False, 2:True).

      - Has ``Diagnosis`` which also appears in ``SUM`` as final diagnosis?

.. warning:: The excel worksheet ``SUM`` (Summary) ...

      - It is not being extracted yet.

.. warning:: The excel worksheet ``AE`` (???) ...

      - It is not being extracted yet.

.. warning:: The excel worksheet ``EVO`` (???) ...

      - What is ``Pulse20`` and how it relates with ``MaxPulse``?

      - What is ``Heart`` and ``HeartDetails``? The ``Heart`` variable
        has boolean values (1, 2) amd heart details is in Vietnamese with
        values such as fast. Could it be heart_sound_abnormal? Note that
        the ``HeartDetails`` values NHANH appears with both 1 and 2.

      - What is ``Lung`` and ``LungDetails``? Could it be chest_sound or
        chest_sound_right and chest_sound_left?

      - What does the ``R`` mean in ascites, ascitesR, jaundice, jaundiceR,
        vomiting, vomitingR, abdopain, abdopainR? At the moment assume level.

.. warning:: The excel worksheet ``ULTRA`` (Ultrasound) ...

      - Has ``side`` probably referred to ``PleuralEffusion` with values 2
        and 3. However, there is no conversion to know which one refers to
        left and which one to right.

      - Because these variables are collected from an ultrasound, should
        they be renamed different (e.g. ultrasound_ascites) compared to
        others in which they are suspected but not verified with ultrasound?

.. warning:: The excel worksheet ``MGMT`` (Management) ...

      - It is not being extracted yet.

.. warning:: The excel worksheet ``DRUG`` (Drug) ...

      - It is not being extracted yet.

.. warning:: The excel worksheet ``FU`` (Follow-up) ...

      - Needs revision.

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_06dx.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>








The 13dx dataset
----------------

Recruitment occurred in the public sector outpatient departments of Children’s Hospital No. 1
(HCMC), Children’s Hospital No. 2 (HCMC), The Hospital for Tropical Diseases (HCMC),
Tien Giang Provincial Hospital, Dong Nai Children’s Hospital, Binh Duong Provincial Hospital and Long
An Provincial Hospital. These outpatient departments function as primary care
providers to their local communities. A patient presenting to one of the study sites was eligible
for enrolment if they met the following inclusion criteria—a) fever at presentation (or history
of fever) and less than 72 hours of symptom history, b) in the attending physicians opinion
dengue was a possible diagnosis, c) 1–15 years of age inclusive, d) accompanying family member or
guardian had a mobile phone and e) written informed consent for the child to participate was provided
by the parent/guardian. Patients were excluded if- a) the attending physician
believed they were unlikely to be able to attend follow-up or b) the attending physician believed
another (non-dengue) diagnosis was more likely. Patient enrolment occurred consecutively
during normal clinical hours on weekdays without restriction. All patients were enrolled into
the study before the attending physician received the results of any routine laboratory tests.

.. note::

    - I could not find ``event_death``? There is the option if using the outcome ('Died') and
      the date of discharge. But this is still pending on having such information in
      the dataset (check).

    - Does it have enough laboratory? Is these data only for those admitted?

.. warning:: The excel worksheet ``ENROL`` (enrolment):

    - For those variables with Hist used DateIllness for the others DateEnrolment.

.. warning:: The excel worksheet ``DAILY`` (daily):

    - has ``StudyDay`` which probably counts from enrolment (different from DayIllness)
    - has ``NoSymp``, what is this?

.. warning:: The excel worksheet ``INPFU`` (...?):

    - has ``SignCNS`` which is similar to ``CNS``. I think ``CNS`` is either ``SignCNS``
      or ``LowerGCS`` which is calculated with the other glasgow comma score related
      columns.

.. warning:: The excel worksheet ``SEROLOGY`` (serology):

    - what is ``DateIllness`` and ``SampleDOI``? Is DateIllness the event_onset?
      Never mind, they are all blank values.

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_13dx.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>









The 32dx dataset
----------------

We performed a STROBE-compliant prospective observational study at the National Hospital for Tropical Diseases
(NHTD), Hanoi, Vietnam, between June 2013 and February 2014. Ethical approval was obtained from the Oxford Tropical
Research Ethics Committee and the Ethics Review Committee at NHTD, and written informed consent was obtained from
all participants or the parents/guardians of children. Adults and children >5 years of age with a clinical diagnosis
of possible dengue were eligible for enrollment into either of 2 study arms. In the outpatient arm, participants
presenting within 72 hours of fever onset could be enrolled if no alternative cause for the fever was identified.
For the inpatient arm, any patient admitted to NHTD with suspected dengue with warning signs or severe dengue was
eligible. All patients were reviewed daily until fully recovered and afebrile, or for up to 6 days after enrollment.
Standardized clinical information was recorded daily, including findings of detailed clinical examination and
hemodynamic assessment. A complete blood cell count was performed daily, with additional samples obtained
for a biochemical profile and dengue diagnostics at enrollment, at defervescence, and at a follow-up visit 10–14
days after illness onset. Any outpatient requiring admission continued to be followed up daily in hospital, with
the indication for admission documented, and all management interventions were recorded. Additional investigations,
including ultrasonography and/or chest radiology, were performed if clinically indicated.

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_32dx.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>

.. note::

      - No DayIllness

.. warning:: The excel worksheet ``HIS`` (history) ...

      - The ``Other`` is boolean. It represents other comorbidities and
        these are specified in the ``Detail`` variable.

      - Assumed ``DateFever`` as ``event_onset``.


.. warning:: The excel worksheet ``HIS`` (history) ...

      - Has ``HeartSound`` with all values as 1. Then because the variable
        ``HeartSoundDesc`` is all blank, a value of 1 in HeartSound means
        that the heart sound was normal (heart_sound_abnormal; 1:False, 2:True).

      - Assumed ``ifPal1`` refers to liver_palpation_size

      - ASsumed ``ifPal2`` refers to spleen_palpation_size.


.. warning:: The excel worksheet ``EVO`` (evolution) ...

      - Assumed that ``IsFever`` refers to whether the patient has fever
        on such date and therefore recorded as ``event_fever``.

.. warning:: The excel worksheet ``SUM`` (summary) ...

      - Not extracted yet.

.. warning:: The excel worksheet ``LAB`` (summary) ...

      - StudyDay probably refers to date_admission (or date_enrolment).

.. warning:: The excel worksheet ``FU`` (follow up) ...

      - DayFinalAss (only values from 2 to 4.
      - Not extracted yet.

.. warning:: The excel worksheet ``NS1`` (ns1)...

      - It is completely empty.

.. warning:: The excel worksheet ``LAB_DIAGNOSIS`` (ns1)...

      - Contains data that mostly can be extracted from other tabs.


The 42dx dataset
----------------

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_42dx.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>



.. warning::

    - Needs thorough reporting as the others.





The 01nva dataset
-----------------

.. warning::

        - ``FLUIDS`` related information has not been extracted yet.
        - ``TREATMENT`` related information has not been extracted yet.

.. warning:: The excel worksheet ``DM``...

        - stands for ...? DM =

.. warning:: The excel worksheet ``HIST`` (History) ...

        - Has the following fever related columns (``FEVERDTC``, ``FEVERTIME`` and ``FEVERDAY``).
          What does ``FEVERDAY`` represent with respect to the others? Note that ``FEVERDAY`` has
          (almost) always a value whereas the others are only filled for a few of the patients. In
          addition, fever day is only missing in some cells when fever day is actually available...?

          In general, it looks like these columns might match the equation (date_fever + day_fever =
          date_admission) but there are some cases in which it does not (e.g. ...):

                - 003-2232 - fever 12/12/20 - day fever 5 - admission 12/15/20

        - Most of the date columns are not available in all the rows (patients) except for the
          ``date_gemonitor`` and ``enteredtime``. Therefore, how can I assign a date to the
          vital signs collected and/or the day of fever? Ideally day of fever or day of admission
          but they are often missing. At the moment copied admission from ED worksheet because
          the ``enteredtime`` time in many occasions has delays (e.g. ED worksheet).

        - The admission date from the worksheets ``HIST`` and ``ED`` does not match.
        - The GE monitors have ``date_start`` but not ``date_end`` (maybe because it is ongoing?)

        - Has entered time which ...

            003-1101 - enteredtime 6/05/20

.. warning:: The excel worksheet ``ED`` (Emergency Deparment)...

        - has ``NS1AG``. Any form of getting the igm/igg date, value and interpretation?
          Also it has the values 'NA', 'Pos', 'Neg', 1 and 2. I have assumed that 1 also
          represents 'Positive' and 2 represents 'Negative'. What is AG?

.. warning:: The excel worksheet ``ES`` (??????) ...

        - does not have other date column than ``enteredtime``. However, this ``enteredtime``
        might not be the exact time in which the events happened. In other worksheets the
        ``enteredtime`` columns show some delay and there are additional date columns such
        as date_sample. Anyways at the moment assume such column as the right time.

.. warning:: The excel worksheet ``CLI`` (Clinical)...

       - Remember to double check that all date_start entries have date_end.

.. warning:: The excel worksheet ``DIS`` (Discharge)...

       - Can ``DATEASSES`` be interpreted as date_discharge?
       - has ``NS1IGM``. Any form of getting the igm/igg date, value and interpretation? Is
         this NS1 representing both IGM/IGM single/paired results? For instance the
         igm_interpretation and igg_interpretation would be useful to compute both the single
         and the paired interpretations.

.. warning:: The excel worksheet ``DAY`` ...

       - has the column ``DAY``. Is it day from admission? day from enrolment? day from onset?

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_01nva.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>







.. |pdf-lam2013| image:: ../_static/pdf-icon.png
   :target: ../_static/datasets/manuscripts/lam2013.pdf
   :scale: 5%
   :alt: pdf

.. |pdf-lam2015| image:: ../_static/pdf-icon.png
   :target: ../_static/datasets/manuscripts/lam2015.pdf
   :scale: 5%
   :alt: pdf

.. |pdf-lam2017| image:: ../_static/pdf-icon.png
   :target: ../_static/datasets/manuscripts/lam2017.pdf
   :scale: 5%
   :alt: pdf

.. |pdf-nguyen2013| image:: ../_static/pdf-icon.png
   :target: ../_static/datasets/manuscripts/nguyen2013.pdf
   :scale: 5%
   :alt: pdf

.. |pdf-nguyen2017| image:: ../_static/pdf-icon.png
   :target: ../_static/datasets/manuscripts/nguyen2017.pdf
   :scale: 5%
   :alt: pdf

.. |pdf-tam2012| image:: ../_static/pdf-icon.png
   :target: ../_static/datasets/manuscripts/tam2012.pdf
   :scale: 5%
   :alt: pdf

.. |pdf-the2012| image:: ../_static/pdf-icon.png
   :target: ../_static/datasets/manuscripts/the2012.pdf
   :scale: 5%
   :alt: pdf

.. |pdf-tien2013| image:: ../_static/pdf-icon.png
   :target: ../_static/datasets/manuscripts/tien2013.pdf
   :scale: 5%
   :alt: pdf

.. |pdf-tuan2015| image:: ../_static/pdf-icon.png
   :target: ../_static/datasets/manuscripts/tuan2015.pdf
   :scale: 5%
   :alt: pdf

.. |pdf-wills2005| image:: ../_static/pdf-icon.png
   :target: ../_static/datasets/manuscripts/wills2005.pdf
   :scale: 5%
   :alt: pdf

.. |pdf-yacoub2015| image:: ../_static/pdf-icon.png
   :target: ../_static/datasets/manuscripts/yacoub2015.pdf
   :scale: 5%
   :alt: pdf

.. |pdf-yacoub2016| image:: ../_static/pdf-icon.png
   :target: ../_static/datasets/manuscripts/yacoub2016.pdf
   :scale: 5%
   :alt: pdf

.. |pdf-yacoub2017| image:: ../_static/pdf-icon.png
   :target: ../_static/datasets/manuscripts/yacoub2017.pdf
   :scale: 5%
   :alt: pdf


******************
Useful definitions
******************

Defining complications
----------------------

Defining dengue interpretation
------------------------------

