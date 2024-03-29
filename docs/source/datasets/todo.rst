Changelog
=========

Versions
--------

.. note:: Not implemented yet.

- v0.0.7

- v0.0.6

- v0.0.5

- v0.0.4

- v0.0.3

- v0.0.2


v0.0.6
~~~~~~

v0.0.5
~~~~~~

v0.0.4
~~~~~~

v0.0.3
~~~~~~

v0.0.2
~~~~~~

v0.0.1
~~~~~~

ToDo
----

.. note:: This section could be directly including through the use of ``github issues``
          where people can report issues or new features, label their type (fix,
          hot fix, enhancement), comment on them and close them when solved. However,
          todo list has been included here at the moment for simplicity.

.. todo:: ``.zip file``

    Automatically create .zip file with version tag including:

     - the ccfg.xlsx configuration files
     - the corrector.yaml file
     - the information with main changes

.. todo:: ``Booleans to Categories``

    Allow to combine features that have been recorded as booleans in different
    columns into a single column with several categories. See the example below
    for ventilation with ['Cannula', 'Mechanical', 'NCPAP']

      - ventilation_cannula    - boolean
      - ventilation_mechanical - boolean
      - ventilation_ncpap      - boolean

.. todo:: The ``string features`` need formatting...

    There are many string columns that have been inputed manually and which might
    need exhaustive cleaning. They usually include antimicrobial dose, frequency,
    via of administration and fluids. Some bleeding has also recorded in text
    format. In addition, look at features as occupation, hospital, district,
    ward, ...

    Possible things to consider:

       - Trimming and duplicated spaces
       - Uppercase, lowercase and Capitalized
       - Abbreviations Hosp. and Hosp
       - Misspelling errors
       - ...

.. todo:: ``Examples`` to include in the galleries...

       - ``Date in which features are available``: Graphs showing when features are
         usually available taking into account the three disease timelines; that is,
         day_from_onset, day_from_admission and day_from_enrolment. It would be also
         possible to define a day of defervescence.

       - ``Description of the datasets``: Autogenerated description of the datasets
         according to any specific outcome, the presence of dengue, complications,
         and other. Include n_patients, distributions and percentages for age,
         gender, weight, height, ..... - PARTIALLY IMPLEMENTED!


.. todo:: What to do with ``liver`` related features?

    - liver_acute
    - liver_failure
    - liver_involved
    - liver_mild
    - liver_severe
    - liver_palpation
    - liver_palpation_size
    - liver_size (liver_palpation_size)

.. todo:: Issues and considerations related with ``events``...

    When comparing the events' count:

    - In particular event_admission, event_discharge should have the same numbers
      in the counts table, however, this does not always the case. Wondering whether
      maybe events_transferred should also be considered as discharged. Any other
      suggestions?

    - Count the number of different study_no's in each database, it might help.

    - In the case of event_onset, there should be always more than admissions.

    - In 32dx review event_death; all the patients died!. In the 'SUM' worksheet
      the DeathDate and DeathTime is filled for all the records.

    - What about event_followup? Sometimes really high numbers!



.. todo::

  - ``event_death``
      - There should not be any date after ``event_death``.
      - If ``outcome`` == 'Died' set ``event_death`` == True for day of last data.

  - There can be data after event_discharge (because of the follow ups).

  - If outcome is 'Full Recovery' then we can set up the event_discharge
    as the last day with values (if no event_follow up). Also review
    inconsistencies between outcomes (Died) and events.

  - If outcome is 'Died' then if event_admission then add event_discharge.
    The event_discharge could be placed the last day values were recorded,
    and in addition, event_death should be set too.

  - When compute patient length stay, or when setting any discharge date
    be careful with the follow up dates.

  - The day_from_onset has sometimes negative values which should not happen.
    Thus, have a thorough look at this. There are date errors in the data,
    think how to address this issues or just discard such patients. Maybe
    remove my day cleaner? There was also one data with marge datetime
    formats? and also giving error and had to use coerce?

  - Related with shocks:

     - If event_shock count == 1: shock = 1
     - If event_shock count >= 1: shock = 1 / shock_multiple = 1
     - There are also two weird variables, shock_no and shock_time. These
       variables might also be used to increase the accuracy of the shock
       event tracking?

  - event_onset < event_admission
  - event_admission < event_discharge
  - event_admission < event_enrolment. It depends??
  - event_shock can happen at any time
  - event_shock missing in some datasets
  - if there is an event_admission for a patient, then there should be an
    event_discharge, event_transferred or event_death.

  - ``Fever``: This value has been collected in many different types, sometimes
    just the presence of fever was recorded, sometimes the body temperature was
    recorded and sometimes both have been recorded. To ensure that all values
    are consistent:

    - if body_temperature > 37.5 then create event_fever for that date.
    - if body_temperature < 37.5 there might still be an event_fever, note
      that temperature values are just collected once per day. I assume then
      keep both.

.. todo:: Other...

    - ``gcs`` as a sum of other gcs subcategories.
    - Let users apply the range filters if they want too?

    - Do check levels (e.g. abdominal_pain, abdominal_pain_level) and whether
      this were levels or days. Oh dear!

.. warning::

    ``Damien`` => datasets comments (manuscript):

    - Patients enrolled in the intervention arm of the randomised control trial 06DX
      were then removed (n=150), as were patients who were not admitted to hospital and
      managed in the community – this consisted of the majority of patients in 13DX
      which was an outpatient-based study.

    - For patients who experienced a complication of dengue (shock, significant effusion
      or significant bleeding) we discarded all entries obtained on, and after that date.
      For patients who did not experience complication in dengue, we used a median illness
      day of 5 (i.e. up to 120 hours after onset of illness where start of illness is
      represented by day 0) as the cut-off and discarded all observations after that date
      (n=214).

    - This formed the final dataset used for analysis (n=4,231 patients) - see table 1 in
      main text for  summary of patients included in this dataset.


.. warning::

    ``Damien`` => clinical overview of dengue:

    We think of dengue as very much a disease which follows certain phases (whether this
    is right or wrong!) – typically, people experience:

    - The febrile phase (days 1-5) – they are unwell with fever, but no life threatening
    clinical manifestations happen.
    - The critical phase (days 4-6+) – they are in danger of being critically unwell e.g.
    they are in shock, bleed a lot, or need therapy (fluids, ventilation etc)
    - The recovery phase (after days 6+) – after the critical phase.

    The two main questions that people have typically felt are important for clinical
    management are: When I see someone presenting with a fever, is this dengue, or another
    disease (e.g. a bacterial infection)? Dengue doesn’t require antibiotics for bacterial
    infections (including sepsis) do. The pattern of illness and how you manage the patient
    also matters (e.g. do you discharge them, or admit them to hospital). For someone with
    dengue, what is the risk of them developing severe dengue (shock, bleeding, plasma leak)?
    When in the illness time-course can I reliably predict this? What measurements do I need?

    Be aware that the data is imperfect however, with a lot of missingness – and the time
    element of the observations is crucial (febrile-critical-recovery model of disease).
    For example: examination findings are probably more subjective and open to interpretation
    compared with laboratory values, and the measurement of outcomes likewise can vary between
    studies.

    Finally the studies themselves are comparable to a certain extent, but do differ in how
    they recruit their patients e.g. 13DX recruits patients early in illness when presenting
    to their local health centre, MD recruits after admission, and DF recruits after they enter
    intensive care. The day of illness is therefore key to aligning all the studies for
    comparison.

Useful .rst syntax
------------------

Using literalinclude is fragile and can break easily when examples are changed (all the more when
line numbers are used instead of start-after and end-before). Use with caution: linking directly
to examples is a more robust alternative.

.. literalinclude:: ../examples/plot_0_sin.py
   :language: python
   :start-after: # License: BSD 3 clause
   :end-before: # To avoid matplotlib