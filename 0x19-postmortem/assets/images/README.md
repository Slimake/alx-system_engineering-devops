# Postmortem: The Great Write Stampede of 2024
Incident Date: Sat Aug 17 2024 19:42:28 UTC  
Duration: 2 days  
Severity: low (phew "What a relief")  
Impact: Our database servers went from "quietly writing data" to "trying to be the next Enimem" with a record-breaking number of writes per second. Spoiler alert: they didn't win any awards.

![write](../assets/images/write.jpg)

> ## Issue Summary
> Duration of the outage:
> * Start time - Sat Aug 17 2024 19:42:28 UTC
> * End time - Mon Aug 19 2024 16:24:09 UTC
>
> Impact of service:
> * The service was not impacted in anyway
>
> Root cause:
> * The root cause was the evaluated value was above the alert threshold value set in the monitoring tool

> ## Timeline
> When was issue detected:
> * time - Sat Aug 17 2024 19:42:28 UTC
>
> How was the issue detected:
> * time - Sat Aug 17 2024 19:42:28 UTC
> * A monitoring alert tool(Datadog)
>
> Actions taken:
> * time - Mon Aug 18 2024 19:35: 09 UTC
> * The writes per second operation on the server was measured
>
> Misleading investigation/debugging:
> * time - Sat Aug 18 2024 19:42:28 UTC
> * No misleading debugging paths as the monitoring tool stated clearly what happened
>
> Which team/individuals was the incident escalated to:
> * time - Sat Aug 17 2024 19:49:28 UTC
> * My supervisor
>
> How was the incident resolved:
> * End time - Mon Aug 19 2024 16:24:09 UTC
> * By setting the right threshold value

> ## Root cause and resolution
> Explanation in detail on what was causing the issue:
> * The threshold value set in the monitoring tool was too low. I wasn't sure of the value to set initially so i set it to a random value
>
> Explanation in detail on how the issue was fixed:
> * By setting the right threshold value. The value was determined after studying the write per second and then applying it to the monitoring tool
>
> ## Corrective and preventative measures
> Things that can be improved:
> * Faced with monitoring the write per second next time, we first monitor the write per second on the server and then set an appropriate threshold value for it in the monitoring tool
>
> A list of tasks to address the issue:
> * Measure the write per second value
> * set the right threshold value in the monitoring tool
