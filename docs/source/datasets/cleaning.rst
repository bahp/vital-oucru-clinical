The cleaning process
====================

For this purpose ``DataBlend`` was used.

``DataBlend`` is a lightweight library to format manually collected data. It allows
to perform common transformations (e.g. rename or replace) and conversions to various
data structures such as **stacked** data structure used in databases or **tidy** data
structure used in AI/ML libraries.

The code of the project is on Github: https://github.com/bahp/datablend


Naming conventions
------------------

In general, use variable names to describe the data collected using
the most meaningful word first. Try to include further description of
the variable if possible and avoid using acronyms (unless they are very
well known). Words should be separated by ``_``.

.. note::
  It is very easy to sort variable names alphabetically and using
  good naming conventions will make them appear together. This will
  facilitate further inspection to validate the results.

Example with ascites:

.. code::

    ascites                  # boolean (presence of ascites)
    ascites_level            # number or str ([1,2,3], [Low, Medium ,High])
    ascites_description      # free-text
    ascites_interpretation   # interpretation by clinicians
    ascites_duration         # number (seconds, minutes)

Example with bleeding:

.. code::

    bleeding          # compound feature (any bleeding)
    bleeding_skin     # bleeding in skin
    bleeding_gum      # bleeding in gum
    bleeding_mucosal  # bleeding in ...
    bleeding_gi       # bleeding in gastro-intestinal
    bleeding_vaginal  # bleeding in vagina
    bleeding_other    # bleeding in other site

Example with shock:

.. code::

    shock              # whether shock happened during the stay
    shock_multiple     # whether multiple shocks happend during the stay
    shock_clinical     # whether ...
    shock_resucitation # whether ...

Suffixes
~~~~~~~~

level
*****

In the scenario in which we want to indicate the level of a variable,
use the desired variable name and append the word level. Note that level should
be an Integer. Also note that the variable level already contains the boolean
variable since 0 can be mapped to False and any other number to True

.. code::

    headache         # boolean (presence of headache)
    headache_level   # Int64 (intensity of the headache)

abnormal
********
Ensure to include the suffix abnormal. For example, instead of
recording heart_sound which seems to indicate whether the heart was beating
or not, be more specific using abnormal. Thus heard_sound_abnormal clearly
specifies that there is some condition to investigate.

.. code::

    heart_sound_abnormal              # There is an abnormal heard sound
    heart_sound_abnormal_description  # Description of the abnormality

description
***********

.. code::

    heart_sound_abnormal              # There is an abnormal heard sound
    heart_sound_abnormal_description  # Description of the abnormality


interpretation
**************

.. code::

    igm_interpretation # string (Positive, Negative, Equivocal)
    igg_interpretation # string (Positive, Negative, Equivocal)
    ns1_interpretation # string (Positive, Negative, Equivocal)
    serology_single_interpretation # string (Primary, Secondary, Not Dengue)
    serology_paired_interpretation # string (Primary, Secondary, Not Dengue)
    dengue_interpretation # boolean


left/right
**********

.. code::

    pleural_effusion       # Any pleural effusion.
    pleural_effusion_left  # boolean
    pleural_effusion_right # boolean
    pleural_effusion_side  # Still pending (e.g. 'Left', 'Right')

percent
********

Those laboratory results with unit expressed in percentages (%) have such information
appended in the variable name. This is to differentiate when the biochemical marker
is measured in percent or in another concentration unit (e.g. mmol/L). Note that there
are many different concentration units that could be used.

.. code::

    monocytes            # concentration (U/mL)
    monocytes_percent    # percentage (%)

duration
********

.. note:: Pending...

Prefixes
~~~~~~~~

event
*****

The event variables have the 'event' prefix in the name.

.. note:: Ensure that laboratory dates (e.g. pcr, serology, cytokines, blood, ...)
  are referring to the sample collection date or the date the laboratory result
  was presented to the clinicians. In some scenarios this information is missing
  in the datasets and other standard dates (e.g. date of enrolment or date of
  admission) have been used. Thus collecting events in this scenarios might
  lead to confusion.

.. code::

    event_onset       # onset of disease
    event_admission   # admitted to hospital
    event_enrolment   # enrolled in the study
    event_laboratory  # sample collected for laboratory test
    event_pcr         # sample collected for pcr test
    event_serology    # sample collected for serology
    event_transfer    # transferred to other unit
    event_discharge   # discharged from hospital (alive/death?)
    event_death       # death

xray
****

.. note:: Pending...

ultrasound (uss)
****************

.. note:: Pending... there are both uss and ultrasound at the moment?

day_from
********


   .. todo:: Include further considerations (or just the links) related to:

        - The generic corrections implemented (static_correct, level_correction,
          compound_feature_correction, replace_correction, order_of_magnitude_correction,
          range_correction, ...)
        - The specific oucru corrections implemented.


Filling empty values (NaN)
--------------------------

.. note:: Pending...

Ensuring consistency
--------------------

.. note:: Pending...

Notes
-----

This section includes questions for each specific dataset. The questions are divided
for each dataset and subdivided by the excel worksheet in which the variables
appear.

The df dataset
~~~~~~~~~~~~~~

.. warning::

    - Worksheet ``DF``:

        - Need to clarify when things happened, there are various dates (e.g., admission,
          enrolment, ...) and all the features for the patient have been included in this
          worksheet. Need to understand what date to assign to each feature.
        - The features ``new_xxxx`` are being also associated with date_admission.
        - There are follow up features but no date_followup.
        - What are ``hemo`` and ``hemo2``?
        - What are ``d1`` and ``d2``?
        - It needs ``reviewing``!


The fl dataset
~~~~~~~~~~~~~~

.. warning::

    - Worksheet ``FL_CLINICAL_SUM`` (clinical summary):

        - Has ``vomitHis``, ``vomitExam`` and ``vomit``. Should they be assigned
          to date_onset, date_admission and date_enrolment respectively? Or maybe
          we should swap date_enrolment and date_admission?
        - It needs ``reviewing``!

    - Not all worksheets have been included!


The md dataset
~~~~~~~~~~~~~~

.. warning::

    - Worksheet ``MD_lab`` (laboratory):

        - What is ``from_adm``? It is probably day_from_admission.

    - Worksheet ``MD_clinical`` (clinical):

        - ``day_ill`` with respect to date_admission? date_enrolment? date_fever?

        - ``bleeding`` contains categories (No, skin only and mucosal) wich have
          just been converted to booleans. However, not sure what date to use. Since
          it is a compound we are not retrieving it as we have the subcategories
          (Skin, mucosal).

        - Do the variables ``sigbled``, ``sigbled_s``, ``bleed_hos``, ``overload``
          and others around refer to date_admission or date_discharge?

        - what is ``d2shock``?

    - Worksheet ``MD_PCR`` (PCR):

        - Only extracting the summary columns serotype and viremia.

    - Worksheet ``MD_Tien_hist`` (history) :

        - Ignored, such data looks like it is already in the second sheet (MD_clinical).

    - Worksheet ``MD_Tien_exam`` (examination):

        - Ignored, such data looks like it is already in the second sheet (MD_clinical).

    - Worksheet ``MD_Tien_DRvalue``:

        - Does this data refer to the DR dataset? If so ignore worksheet.
        - Ignored, such data looks like it is already in the third sheet (MD_PCR).
        - It has 6100 rows!, while clinical has only 3020. Maybe contains DR, DF and MD.
        - It is missing a datetime column.

    - Worksheet ``MD_Tien_invest``:

        - Ignored, such data looks like it is already in the second sheet (MD_clinical).
        - It has 3400 rows! while clinical has only 3020.


The dr dataset
~~~~~~~~~~~~~~

.. warning::

    - Worksheet ``DR1_2232_ENROL`` (PCR):

        - It needs ``reviewing``!

    - Worksheet ``NEGATIVE_LIST_STUDY`` (PCR):

        - has ``day of illness`` not clear what datetime to assign it. It only has
          the datetime columns date_fu and date_fever?



The d001 dataset
~~~~~~~~~~~~~~~~

.. warning::

    - Worksheet ``D001_CLINICAL``:

        - has ``day of illness`` not clear what datetime to assign it, should it be
          date_admission or date_enrolment?

        - No categories specified for ``outcome`` with encoded values 1, 2, 3, 4.

    - Worksheet ``D001_LAB``:

        - Is the ``inmune status`` related with the serology interpretations? In
          particular with the value secondary taht indicates whether the patient
          had suffered from dengue before.

    - Worksheet ``D001_SERO_DATA``:

        - Unfortunately it does not have a datetime64[ns] columns. Thus, unless the
          day of illness is present there is no reference date to include it.
        - It needs ``reviewing``! Only basic extracted.

    - Worksheet ``D001_SERO_DATA_INMUNE``:

        - Unfortunately it does not have a datetime64[ns] columns. Thus, unless the
          day of illness is present there is no reference date to include it.
        - It needs ``reviewing``! Only basic extracted.

    - Worksheet ``D001_SERO_DEMO`` (PCR):

       - Ignored, repeated from first sheet.


The 06dx dataset
~~~~~~~~~~~~~~~~

.. note::

  - Bleeding severity (1 - only skin, 2 mild mucosal +/- skin and 3 severe either mucosal or skin)

.. warning::

    - Worksheet ``SCR`` (???)

        - Has ``Pregnant`` and ``PregnancyPos``. All the values for both are 2,
          which I assume is False (based on other datasets). However, it has been
          collected that they might actually represent only those who were
          pregnant?

    - Worksheet ``HIST`` (History)

        - Has ``Dayillness``, match with date_admission or date_enrolment?

        - Has ``HeartSound`` with all values as 1. Then because the variable
          ``HeartSoundDesc`` is all blank, a value of 1 in HeartSound means
          that the heart sound was normal (heart_sound_abnormal; 1:False, 2:True).

        - Has ``CNS`` with all values as 1. Then because the variable
          ``CNSDesc`` is all blank, a value of 1 in CNS means
          that the CNS was normal (cns_abnormal; 1:False, 2:True).

        - Has ``Diagnosis`` which also appears in ``SUM`` as final diagnosis?

        - One date has a bad time format (24:00 should be 00:00).
        - The date of fever has been used for all the history symptoms.

    - Worksheet ``SUM`` (Summary)

        - It is not being extracted yet.

    - Worksheet ``AE`` (???)

        - It is not being extracted yet.

    - Worksheet ``EVO`` (???)

        - What is ``Pulse20`` and how it relates with ``MaxPulse``?

        - What is ``Heart`` and ``HeartDetails``? The ``Heart`` variable
          has boolean values (1, 2) amd heart details is in Vietnamese with
          values such as fast. Could it be heart_sound_abnormal? Note that
          the ``HeartDetails`` values NHANH appears with both 1 and 2.

        - What is ``Lung`` and ``LungDetails``? Could it be chest_sound or
          chest_sound_right and chest_sound_left?

        - What does the ``R`` mean in ascites, ascitesR, jaundice, jaundiceR,
          vomiting, vomitingR, abdopain, abdopainR? At the moment assume level.

    - Worksheet ``ULTRA`` (Ultrasound)

        - Has ``side`` probably referred to ``PleuralEffusion`` with values 2
          and 3. However, there is no conversion to know which one refers to
          left and which one to right.

        - Because these variables are collected from an ultrasound, should
          they be renamed different (e.g. ultrasound_ascites) compared to
          others in which they are suspected but not verified with ultrasound?

    - Worksheet ``MGMT`` (Management)

        - It is not being extracted yet.

    - Worksheet ``DRUG`` (Drug)

         - It is not being extracted yet.

    - Worksheet ``FU`` (Follow-up)

         - It needs ``reviewing``!




The 13dx dataset
~~~~~~~~~~~~~~~~

.. note::

    - I could not find ``event_death``? There is the option if using the outcome ('Died') and
      the date of discharge. But this is still pending on having such information in
      the dataset (check).

    - Does it have enough laboratory? Is these data only for those admitted?

.. warning::

    - Worksheet ``ENROL`` (enrolment):

        - For those variables with Hist used DateIllness for the others DateEnrolment.

    - Worksheet ``DAILY`` (daily):

        - has ``StudyDay`` which probably counts from enrolment?
        - has ``StudyDay`` which is different from DayIllness.
        - has ``NoSymp``, what is this?

    - Worksheet ``INPFU`` (inpatient followup):

        - has ``SignCNS`` which is similar to ``CNS``.
        - has ``CNS`` which I think it is either ``SignCNS`` or ``LowerGCS``. The latter
          is calculated with the other glasgow comma score related columns for eye,
          motor and xxxx.

    - Worksheet ``SEROLOGY`` (serology):

        - what is ``DateIllness`` and ``SampleDOI``? Is DateIllness the event_onset?
          Never mind, they are all blank values.




The 32dx dataset
~~~~~~~~~~~~~~~~

.. note::

      - No DayIllness

.. warning::

    - Worksheet ``HIS`` (history) ...

        - The ``Other`` is boolean. It represents other comorbidities and
          these are specified in the ``Detail`` variable.

        - Assumed ``DateFever`` as ``event_onset``.


    - Worksheet ``HIS`` (history) ...

      - Has ``HeartSound`` with all values as 1. Then because the variable
        ``HeartSoundDesc`` is all blank, a value of 1 in HeartSound means
        that the heart sound was normal (heart_sound_abnormal; 1:False, 2:True).

      - Assumed ``ifPal1`` refers to liver_palpation_size

      - ASsumed ``ifPal2`` refers to spleen_palpation_size.


    - Worksheet ``EVO`` (evolution) ...

      - Assumed that ``IsFever`` refers to whether the patient has fever
        on such date and therefore recorded as ``event_fever``.

    - Worksheet ``SUM`` (summary) ...

      - Not extracted yet.

    - Worksheet ``LAB`` (summary) ...

      - StudyDay probably refers to date_admission (or date_enrolment).

    - Worksheet ``FU`` (follow up) ...

      - DayFinalAss (only values from 2 to 4.
      - Not extracted yet.

    - Worksheet ``NS1`` (ns1)...

      - It is completely empty.

    - Worksheet ``LAB_DIAGNOSIS`` (ns1)...

      - Contains data that mostly can be extracted from other tabs.


The 42dx dataset
~~~~~~~~~~~~~~~~

.. warning::

    - Needs thorough reporting as the others.



The 01nva dataset
~~~~~~~~~~~~~~~~~

.. warning::

        - ``FLUIDS`` related information has not been extracted yet.
        - ``TREATMENT`` related information has not been extracted yet.

.. warning::

    - Worksheet ``DM``

        - stands for ...? DM =

    - Worksheet ``HIST`` (History)

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

    - Worksheet ``ED`` (Emergency Deparment)

        - has ``NS1AG``. Any form of getting the igm/igg date, value and interpretation?
          Also it has the values 'NA', 'Pos', 'Neg', 1 and 2. I have assumed that 1 also
          represents 'Positive' and 2 represents 'Negative'. What is AG?

    - Worksheet ``ES`` (??????)

        - does not have other date column than ``enteredtime``. However, this ``enteredtime``
        might not be the exact time in which the events happened. In other worksheets the
        ``enteredtime`` columns show some delay and there are additional date columns such
        as date_sample. Anyways at the moment assume such column as the right time.

    - Worksheet ``CLI`` (Clinical)

       - Remember to double check that all date_start entries have date_end.

    - Worksheet ``DIS`` (Discharge)

       - Can ``DATEASSES`` be interpreted as date_discharge?
       - has ``NS1IGM``. Any form of getting the igm/igg date, value and interpretation? Is
         this NS1 representing both IGM/IGM single/paired results? For instance the
         igm_interpretation and igg_interpretation would be useful to compute both the single
         and the paired interpretations.

    - Worksheet ``DAY``

       - has the column ``DAY``. Is it day from admission? day from enrolment? day from onset?