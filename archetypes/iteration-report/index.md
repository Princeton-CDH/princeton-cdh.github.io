---
title: "{{ dateFormat "Jan 2" (now.AddDate 0 0 -14 ) }} - {{ dateFormat "Jan 2, 2006" (now.AddDate 0 0 -3 ) }}"
date: {{ now.Format "2006-01-02" }}
iteration_start: {{ dateFormat "2006-01-02" (now.AddDate 0 0 -14 ) }}
layout: iterationreport
hideDesignVelocity: true  # control visibility of design chart
slug: "{{ now.Format "02" }}"
---

add summary paragraphs(s) about the iteration

## Demos
* add demo links or screenshots

{{< figure src="featured-###.png" caption="##">}}


{{/* Add feature image as featured- in this directory for list view display */}}






