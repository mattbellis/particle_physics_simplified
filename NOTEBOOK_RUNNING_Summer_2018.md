# Week 1 (5/21/18-5/25/2018)

We found out that if we copy everything to Drive, it is only the *shared* notebooks that have access to all the data and the helper code. 

[Link](http://www.google.com)

We found out that idle VMs on Colab time out after 90 minutes, and the max lifetime for a VM is 12 hours (source: Stackoverflow). We also found out that you can store 15 gb between gmail, drive, and google photos for free, but G-Suite enterprise, business, or education allows for unlimited storage with 5 or more users, and 1 Tb of storage with 4 or fewer users
As of 7/4/18, Google Colab runtimes seem to allow for 12.73 GB of memory.


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
We began working with HDF5 to interface with CMS, CLEO, and BaBar data.

We recorded a video tutorial on how to use Google Colab, uploaded it to YouTube, and embedded the video onto the site

# Week 4 (6/11/18-6/15/18)
We finished recording video tutorials for the website, uploaded them to YouTube, and then embedded them to the website.

We also updated the activities on the website with the latest version of the h5hep wrapper

There is also a tentative D meson reconstruction activity in the Google Drive folder for Particle Physics Playground that has not yet been added to the website. It is still a work in progress

Added contact chips for the individual contributors to the website

# Week 5 (6/18/18-6/22/18)
Went live with the new design of the website, which Tyler created

Checked the Colab activities to make sure they work; ran into errors with h5hep in the CMS muon and dimuon activities

Began work on answer keys for the activities

More tinkering with the website to see if everything ran smoothly on the new live version

Added an FAQ to the website

# Week 6 (6/25/18-6/29/18)
Uploaded data files to Google Drive and called them in using Python dictionary keys, as well as updating pps_tools to accomodate those files

More sprucing up the notebooks and making sure they work

Looked into pricing options should we choose to store the data on Google Cloud

Experimented with gsutil and os commands to find out how to download data from Google Cloud into Colab

To access data in a Google Cloud bucket, you have to have the permission to read and/or it, or send in a Requester Pays

Also, we found out how to copy over data from a Google Cloud bucket into Google Colab, and then how to access it akin to how we have been doing for the activities on the website

Continued work with BaBar data (now with photons) in the hopes of creating a new exercise for the website

# Future work:

'Verbose' argument in pps tools should be fixed to change output of tools

pps tools should be modified such that the dictionary keys are returned so it is possible to list all the possible keys available for a file
