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
         - ``explore`` more information through the dropdown button (+).
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

.. warning:: Things to highlight.

The trial was a ``single-center``, ``randomized``, ``doubleblind`` comparison of an isotonic
crystalloid solution (Ringer’s lactate) and two isotonic colloid solutions (6% dextran 70
[dextran] and 6% hydroxyethyl starch 200/0.5 [starch]) for emergency resuscitation of
``children`` with ``dengue shock syndrome``. The children were stratified according to pulse
pressure at admission, a marker of the severity of the vascular leak. No children in the group
with severe shock received a crystalloid because of concerns about the potential development of
critical fluid overload without access to advanced respiratory support. The study took place
in the pediatric intensive care unit at the Hospital for Tropical Diseases in Ho Chi Minh City,
Vietnam. The ethics and science committee of the hospital approved the protocol.

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_df.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>



The fl dataset
--------------

.. warning:: Things to highlight.

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_fl.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>



The md dataset
--------------

.. warning:: Important things to consider...

A ``prospective observational study`` of ``children`` hospitalized with ``suspected dengue`` at
the HTD in Ho Chi Minh City, Viet Nam, was conducted between 2001 and 2009. The cohort included
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

The dr dataset
--------------

.. warning:: Important things to consider...

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



The d001 dataset
----------------

.. warning:: Important things to consider...

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_d001.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>



The 06dx dataset
----------------

.. warning:: Important things to consider...

We performed a ``randomized``, ``placebo-controlled``, ``partially blinded`` trial of early
corticosteroid therapy in Vietnamese children and young adults with suspected dengue virus
infection. The study took place on designated infectious diseases wards at the Hospital for
Tropical Diseases of Ho Chi Minh City, with approval from the Ethical Committee of the
Ministry of Health of Vietnam and the Oxford Tropical Research Ethics Committee.

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_06dx.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>



The 13dx dataset
----------------

.. warning:: Important things to consider...

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

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_13dx.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>




The 32dx dataset
----------------

.. warning:: Important things to consider...

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





The 42dx dataset
----------------

.. warning:: Important things to consider...

.. raw:: html

    <iframe src="../_static/datasets/html-tables/features_description_42dx.html"
            frameborder="0"
            scrolling="no"
            height="750px;"
            width="100%"></iframe>




The 01nva dataset
-----------------

.. warning::

        - ``FLUIDS`` related information has not been extracted yet.
        - ``TREATMENT`` related information has not been extracted yet.

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

What is a complication?
-----------------------

    The main complications are ....

       - shock
       - jaundice
       - ascites
       - any other?

Dengue interpretation
---------------------

    .. todo:: Write introduction and includes link to code and method documentation.


    The dengue definition is as follows:

        - positive NS1 point of care assay
        - positive reverse transcriptase polymerase chain reaction (RT-PCR)
        - positive dengue IgM through acute serology
        - seroconversion of either single or paired IgM or IgG samples

    And it is implemented in the following method (link to docs).

    .. code::

        oucru_dengue_interpretation_feature(tidy,
                pcr=True, ns1=True, igm=True, serology=True,
                single_igm_igg=True, paired_igm_igg=True,
                default=False, verbose=10):


Serology interpretation
-----------------------

     .. todo:: Write introduction and includes link to code and method documentation.

     .. include:: <isonum.txt>

     - First igm, igg columns represent 1st sample
     - Second igm, igg columns represent 2nd sample

     .. table:: Overview of serology outcomes from igm and igg
         :widths: 5 5 5 5 10 10 5

         ======== ========= ======== ========= ============= ============= =====
         igm      igg       igm      igg       single        paired        notes
         ======== ========= ======== ========= ============= ============= =====
         |hyphen| |hyphen|  |hyphen| |hyphen|  Inconclusive  Not Dengue
         |hyphen| |hyphen|  |hyphen| |plus|    Inconclusive  Primary
         |hyphen| |hyphen|  |plus|   |hyphen|  Inconclusive  Primary       ``1``
         |hyphen| |hyphen|  |plus|   |plus|    Inconclusive  Primary

         |hyphen| |plus|    |hyphen| |hyphen|  Inconclusive  Inconclusive  ``3``
         |hyphen| |plus|    |hyphen| |plus|    Inconclusive  Secondary*
         |hyphen| |plus|    |plus|   |hyphen|  Inconclusive  Inconclusive  ``3``
         |hyphen| |plus|    |plus|   |plus|    Inconclusive  Secondary*

         |plus|   |hyphen|  |hyphen| |hyphen|  Primary       Inconclusive
         |plus|   |hyphen|  |hyphen| |plus|    Primary       Secondary*
         |plus|   |hyphen|  |plus|   |hyphen|  Primary       Inconclusive  ``1``
         |plus|   |hyphen|  |plus|   |plus|    Primary       Secondary*

         |plus|   |plus|    |hyphen| |hyphen|  Secondary     Inconclusive  ``2``
         |plus|   |plus|    |hyphen| |plus|    Secondary     Secondary*
         |plus|   |plus|    |plus|   |hyphen|  Secondary     Inconclusive
         |plus|   |plus|    |plus|   |plus|    Secondary     Secondary*
         ======== ========= ======== ========= ============= ============= =====


    where

        - * indicates significant increase in igg |
        - ``1`` indicates inconclusive because igg should be |plus| by now |
        - ``2`` indicates it is odd and maybe hovering around the threshold |
        - ``3`` keep it as single outcome. |


    And it is implemented in the following method (link to docs).

    .. code::

        oucru_serology_interpretation_feature(tidy,
                serology_single=True, serology_paired=True,
                serology_interpretation=True,
                inconsistencies='coerce',
                verbose=0):

single igm_igg
~~~~~~~~~~~~~~

paired igm_igg
~~~~~~~~~~~~~~

.. include:: ../../../../../../README.rst
  :start-after: inclusion-marker-do-not-remove

