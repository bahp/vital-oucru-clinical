Notes
=====


.. warning:: When predicting shock, note that some studies did enrol only
             patients once they have had shock. These datasets and/or patients
             should be discarded. Same applies when inferring likelihood of
             severe Dengue.

.. warning:: The studies might have recruited patients at different times. For instance,
             13dx enrolled patients on the early phase whereas XXX enrolled patients
             one they had a symptom. Ideally, day_from_illness (collected by clinicians)
             will give better temporal information.

.. warning:: Note the outliers have not been removed and it has been left at the
             discretion of the user. However, there are clear outliers in parameters
             such as platelets (and many day_from_...).
