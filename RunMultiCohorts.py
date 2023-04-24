import MultiCohortClasses as Cls
import MultiCohortSupport as Support

import EconEvalInputData as D
import ProbilisticParamClasses as P
import deampy.plots.histogram as hist
import deampy.plots.sample_paths as path

N_COHORTS = 20              # number of cohorts
therapy = P.Therapies.MONO  # selected therapy

# create multiple cohort
multiCohort = Cls.MultiCohort(
    ids=range(N_COHORTS),
    pop_size=D.POP_SIZE,
    therapy=therapy)

multiCohort.simulate(sim_length=D.SIM_LENGTH)

# plot the sample paths
path.plot_sample_paths(
    sample_paths=multiCohort.multiCohortOutcomes.survivalCurves,
    title='Survival Curves',
    x_label='Time-Step (Year)',
    y_label='Number Survived',
    transparency=0.5)

# plot the histogram of average survival time
hist.plot_histogram(
    data=multiCohort.multiCohortOutcomes.meanSurvivalTimes,
    title='Histogram of Mean Survival Time',
    x_label='Mean Survival Time (Year)',
    y_label='Count')

# print the outcomes of this simulated cohort
Support.print_outcomes(multi_cohort_outcomes=multiCohort.multiCohortOutcomes,
                       therapy_name=therapy)
