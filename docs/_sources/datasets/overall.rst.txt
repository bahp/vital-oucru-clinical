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
    df      1999-2009 Describe clinical features of ``DSS`` in children   1719
    md      2001-2009 Describe clinical features of ``NSD`` in children   3044
    dr      2005-2008 Describe clinical features of ``NSD`` in children   1165
    06dx    2009-2011 Effect of steroid in Dengue                         75
    13dx    2010-2014 Diagnostic accuracy of NS1                          5729
    32dx    2013-2016 Intravascular volume assessment (CRI)
    42dx
    d001
    01nva   2020-2021
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
all of datasets yet that information will be provided in subsequent sections.

The following table includes:

  - **name:** the name of the feature
  - **dtype:** the data type of the feature
  - **unit:** the unit of the feature (if applicable)
  - **code:**
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
         - ``search`` using the searchbox to filter by any column.
         - ``explore`` more information through the + dropdown.
         - ``export`` the table to any of the available formats.

.. raw:: html

    <iframe src="../_static/corrector.html"
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

    <iframe src="../_static/feature_count.html"
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

The md dataset
--------------

The dr dataset
--------------

The d001 dataset
----------------

The 06dx dataset
----------------

The 13dx dataset
----------------

The 32dx dataset
----------------

The 42dx dataset
----------------

The 01nva dataset
-----------------


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

