# Week 1 (5/21/18-5/25/2018)

We found out that if we copy everything to Drive, it is only the *shared* notebooks that have access to all the data and the helper code. 

[Link](http://www.google.com)

We found out that idle VMs on Colab time out after 90 minutes, and the max lifetime for a VM is 12 hours (source: Stackoverflow). We also found out that you can store 15 gb between gmail, drive, and google photos for free, but G-Suite enterprise, business, or education allows for unlimited storage with 5 or more users, and 1 Tb of storage with 4 or fewer users
An unvarified source claims the VMs run on Google's servers via Colab have roughly 13GB of RAM.


We used Jekyll to create a local version of the website in order to play around with formatting and aesthetics. We found out that this can be done through Notepad on Windows, and XCode on a Mac

We used Bootstrap codes to make the site more user friendly and aesthetically pleasing

## Comments from Dr. Breimer about jekyll site

```html
The root index.html has the following Jekyll code which creates list items (<li>'s) for every activity of a particular category in the _data folder.  In the data folder, you'll find .yml files with the details of each activity.  By the way, in a perfect world, many people could edit and add to these .yml files, which are meant to be very compact and human readable, unlike XML.

	      {% for physbkg in site.data.physics_background %}
	          <li class="list-group-item">
	          	<h5><a href="{{ physbkg.link }}">{{ physbkg.filename }}</a></h5>
	          	<p>{{ physbkg.description }}</p>
	          </li>
	      {% endfor %}	  

I put each category in a card and the activities are list inside the card, but instead of putting each activity in a list item, you could instead generate a card for every activity and then put all the cards in a grid.  That would look something like this

<div class="row justify-content-center">
  {% for physbkg in site.data.physics_background %}
    <div class="col-md-4">
    <div class="card">
           <h5 class="card-header"><a href="{{ physbkg.link }}">{{ physbkg.filename }}</a></h5>
           <div class="card-body">{{ physbkg.description }}</div>
     </div>
     </div>
      {% endfor %}  
</div>
```

# Week 2 (5/28/18-6/1/18)
We found out that Colab works in Google Chrome, Firefox, and Safari, but not in Internet Explorer or Microsoft Edge

We learned how to embed YouTube videos into the website. This will be useful because we recorded tutorial videos which we plan to upload on YouTube and embed those links to help users interact with Colab, the data, and experiment tools.


# Week 3 (6/4/18-6/8/18)
We began working with HDF5 to interface with CMS, CLEO, and BaBar data
