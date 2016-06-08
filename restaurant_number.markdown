
You are probably itching to get to the grades, but first querying the number of restaurants in our dataset is a good sanity check (not to mention easier). In theory, restaurants inspected in a given year should be synonymous with restaurants in operation, since every restaurant is supposed to be inspected at least once a year. If this is true, then we can see the growth (or decline) of the city's restaurant business by plotting the number of restaurants inspected by year as follows.

{% include NYC_restaurants/number_by_year.html %}

Obviously, something's amiss. Such a sharp rise the number of restaurants is implausible in a mature market like New York City, so either the inspections were incomplete in past years or they were incompletely recorded in our dataset. An [official report][] from January 2011 (six months after restaurant grading started)  suggests the latter, speaking of the "10,000 restaurants" that had already graded and the plan to "all of the city's 24,000 restaurants" by Fall 2011. In our dataset, only 21 restaurants were inspected in 2011.

  [official report]: http://www1.nyc.gov/assets/doh/downloads/pdf/rii/restaurant-grading-6-month-report.pdf

The dataset's [accompanying note][] explains why some records may be missing:

  [accompanying note]: https://data.cityofnewyork.us/api/views/xx67-kt59/files/tz91raz45111dHYNIWFwSOksImBbUZ9znxlM4nD_W8A?download=true&filename=About%20NYC%20Restaurant%20Inspection%20Data%20on%20NYC%20OpenData%20082014.docx

> The dataset contains every sustained or not yet adjudicated violation citation from every full or special program inspection conducted **up to three years prior to the most recent inspection** for restaurants and college cafeterias in an active status on the RECORD DATE (date of the data pull).&hellip; Keep in mind that restaurants go in and out of business; **only restaurants in an active status are included in the dataset**.&hellip;
>
>  Because this dataset is compiled from several large administrative data systems, it contains some illogical values that could be a result of data entry or transfer errors. **Data may also be missing.** [Emphasis added.]

Given the three-year retention policy, we cannot expect complete records prior to 4/26/2013. Still, that doesn't explain why some 4000 restaurants appear to be missing from the records in 2014. At 17% of the expected total, it is not likely that they have all gone out of business in less than two years and been removed as a result. That leaves us with only the catch-all explanation: Data is missing.

Fortunately, less data seems to be missing in 2015, with 22,753 restaurants on record or 95% of the expected number. This should be just enough for a representative snapshot of the restaurants and the inspection program. Unless otherwise noted, therefore, **only the 2015 data will be used for all subsequent analysis.**

# Violations

In the chart below are violations found in over 10% of inspected restaurants (hover over a bar for description). The results are somewhat reassuring. The most common violation, affecting more than half of restaurants inspected, is an arcane one having to do *non*-food contact surface. The second most common violation, likewise non-critical, is failure to vermin-proof the facility. Even the top three critical violations are the kinds that one can see committed on a regular basis in a typical household.

{% include NYC_restaurants/violations.html %}

Violations do add up, however. Not only does each violation add to the final score, but each instance of the same violation can raise the score for that violation as well. For example, the most common critical violation, 2G (storing cold food item above 41&deg; F), carries possible scores of 7, 8, 9, 10, and 28. Each improperly stored food item will bump the score up to the next level. This is reasonable. Although individual infractions may seem minor in isolation, together, they can paint a picture of a kitchen in chaos. 

# Score distribution
A look of total scores will therefore be instructive. The chart below shows the score distribution of the 27110 initial inspections that result in valid scores (i.e. excluding the 8 inspections that record scores below 0). 

Overall, NYC restaurants seem to be doing quite well. More than half get an A, and only about 1 in 10 gets a score in the C range (note the language; more on this later).

There is, however, a cloud in that sunny picture. As has been [remarked elsewhere][iqny], the curious dip at scores from 14 to 16 

[iqny] http://iquantny.tumblr.com/post/76928412519/think-nyc-restaurant-grading-is-flawed-heres "I Quant NY"

# Wall of shame
Worse results

