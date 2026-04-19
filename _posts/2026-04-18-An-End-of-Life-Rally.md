---
layout: golden
title: "Why Dying Communities Look Their Best"
date: 2026-04-18
---

In JuliacCon 2025, the conference on the Julia programming language, the [Julia User & Developer Survey](https://www.youtube.com/watch?v=Vh69D04zBtk) was presented. It was conducted over 700 Julia users and developers and they've been doing it in a relatively consistent manner for over 7 years now, which makes it useful to gauge the evolution of the Julia user community.

At first, the findings of the survey look very promising: Julia use continues to climb among Julia users, more users report that it's their favorite language, average number of contributions to the ecosystem has been growing, and the average Julia user has more years of experience than ever before. Just from these observations, one might come to the conclusion that the language, ecosystem, and the community have matured and become more integrated.

However, there was one small statistic briefly mentioned at the start of the presentation that's easy to miss: the number of survey participants a few years ago was over 2000 respondents during the pandemic compared to approximately 700 in 2025. This by itself obviously does not necessarily mean that the number of users shrank by a third. The number of respondents varies yearly and the survey lead said that they're looking into better ways to reach users.

Luckily, one survey question regarding when the user first started using the language, can help uncover what's going on:

![When users started using Julia](/assets/An-End-of-Life-Rally/julia-start-year.png)

Just looking at the plot itself it can be quite difficult to see how the responder demographic looks like. I took the liberty of replotting it to be relative to the year of reply:

![Users relative to year of reply](/assets/An-End-of-Life-Rally/julia-relative-year.png)

A much starker picture appears when looking at the evolution of this curve. You can think of it as the demographic distribution of the age (years of experience with Julia) of survey respondents each year. Early on (2019 up to 2022) there was a healthy curve sloping down, which means that there was a continuous inflow of new users with the most just being a year prior. However, gradually up to 2023 and then sharply in 2024/25, the fraction of newcoming users is much lower than before (going from over 20% to less than 10%) and is no longer the peak of the age demographic. [^1]

With that picture in mind, reexamining the previous promising statistics from the survey paradoxically reveals instead signs of community decline. When observing such a rise in positive metrics such as user satisfaction and average contributions, it is naturally tempting to assume the ecosystem is improving. However, what is likely actually happening is that the influx of newcomers has dropped off, causing the demographics to skew heavily toward veteran community members who have been committed members for a long time. [^2]

Simply, the positive trends are a form of survivorship bias, where the dwindling rate of newcomers boosts up the average values of engagement level. 

In fact, this burst in signs of life following a shock or shrinkage of a group or community is a common phenomenon. Common enough to warrant a term: the Evaporative Cooling effect, coined by AI researcher Eliezer Yudkowsky. Eliezer drew the analogy from how cults tend to become more radicalized following a major shock such as the failure of a prophecy. The skeptical or undedicated members leave, leaving only the most uniquely devoted, highly engaged fanatic core behind.

From a population dynamics perspective, when a community suffers from a reduction in membership inflow, the first symptom is not collapse, but population aging. As the demographic distribution becomes increasingly top-heavy with veteran users, it causes the average engagement and productivity metrics to rise. A well-known instance of this is the demographic dividend: when a country experiences a rapidly declining birthrate, its GDP per capita often inflates for a time simply because of the rising ratio of productive adults compared to new dependents. However, this statistical illusion can misdirect attention away from impending failure. So long as the influx of newcomers persistently fails to offset the exit rate of existing users, this period of apparent prosperity will eventually end, and the total population will significantly shirnk and possibly collapse.

---

[^1]: It should be noted that no blame is being placed on how the survey results were analyzed or presented. As a commenter on the video rightly pointed out, the presenter was given a measly 15-minute timeslot, making it nearly impossible to dive into complex longitudinal demographic shifts.

[^2]: A counter-argument to this demographic paradox is that the userbase is simply maturing. Given that Julia only became available about 15 years ago, the ecosystem may just be abandoning its initial hype cycle and is in the process of settling into a more stable and sustainable community.
