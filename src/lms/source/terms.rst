===============
Terms
===============

.. glossary::
    :sorted:


    Activity
    Activities
    Learning Activity
    Learning Activities
        In SCORM 2004 sequencing, 
        every :term:`item` in a SCORM :term:`manifest` is called an “activity”. 

        Activities can be “**deliverable**”, 
        or “**leafs**” when they correspond to a SCO or Asset. 

        Or, activities can be “**clusters**” 
        when they are aggregations containing child activities.


        .. note::
            - :ref:`scorm_cam.activity`
            - <item> == "activity"
    

    Activity Tree
    活動ツリー 
        The complete set of all activities in a SCORM 2004 course. 

        Activities are nested into parent-child relationships. 

        The complete tree of parent-child relationships is referred to as the “activity tree”. 

        An activity tree generally corresponds to an organization 
        in the SCORM manifest. 
    

    Asset
    Assets
        A reusable piece of training 
        that doesn’t communicate with the LMS. 

        Assets may be a simple collection of files 
        that are used by other resources in a SCORM manifest. 

        Or, 
        assets may be deliverable units of training similar to SCOs. 

        Assets are a type of “:term:`resource`” in the SCORM manifest just like :term:`SCOs`.

        .. note::
            - :ref:`scorm_cam.asset`

    SCO
    SCOs
    Sharable Content Object  
    Sharable Content Objects 
        “Sharable Content Object” – 
        A type of resource that represents the heart of SCORM. 

        SCOs are reusable chunks of training that are assembled into organizations 
        within a :term:`manifest`. 

        Defining content as a set of SCOs enables content to be reused 
        within and across courses.


        .. note::
            - :ref:`scorm_cam.sco`


    Resource
    Resources
    Learning Resource
    Learning Resources
        A discrete reusable unit of training defined in the SCORM :term:`manifest`. 

        Resources are the reusable chunks of learning that comprise a SCORM course. 

        They can be either :term:`SCOs` 
        (the most common type of resource, a unit of training that communicates with the LMS) or 
        :term:`Assets` (simply collections of files that may or may not be deliverable units of training).

        .. note::
            - :ref:`scorm_cam.resources`

    Manifest
    Manifests
    imsmanifest.xml
        A file that describes the contents of a content package. 

        In SCORM, 
        the manifest is always an XML file named 
        “imsmanifest.xml” that is located at the **root** of the content package.

    Organization
    Organizations
    Content Organization
    Content Organizations
        A collection of items in a content package. 

        An organization corresponds to a sequencing :term:`activity tree` 
        and represents one way of aggregating all the resources in a content package. 

        A content package can contain several alternate organizations 
        that each represent a different way of organizing the training 
        (potentially for different intended audiences).

        .. note::
            - :ref:`scorm_cam.content_organization`
            - :ref:`scorm_cam.organizations`

    Aggregation
    Aggregations
    Content Aggregation
    Content Aggregations
        An item in the SCORM :term:`manifest` 
        that contains child items. 

        Corresponds to a “cluster” 
        when referred to in the context of SCORM sequencing.

        .. note::
            - :ref:`scorm_cam.content_aggregation`


    Package
    Content Package
        SCORM courses are meant to be delivered in self contained units. 

        These units are called content packages. 

        The Content Packaging Specification is the part of the SCORM specification 
        that describes how content should be bundled into a package.

        .. note::
            - :ref:`scorm_cam.package`

    Metadata
        Data that describes a SCORM course. 

        The SCORM content packaging specification defines 
        a number of metadata elements 
        that content authors can use to describe their content. 

        Metadata elements include things like, 
        title, description, keywords, educational objectives 
        and technical minimum requirements.

        .. note::
            - :ref:`scorm_cam.metadata`

    Content
        :ref:`scorm_cam.content`


    Item    
        - :term:`Activity`


    PIF
    Package Interchange File
        A SCORM content package is a self-contained ZIP file 
        containing certain contents defined by the SCORM standard. 

        The file is known as a Package Interchange File (PIF) 
        and it contains all files needed to deliver the content package 
        via a SCORM run-time environment and/or learning management system (LMS). 

        Mandatory Content Package contents:

            - XML manifest file (imsmanifest.xml)
            - All schema/definition (.xsd and .dtd) files referenced by the manifest file
            - All resource files used by the content package and its learning activities

        .. note::
            - :ref:`scorm_cam.3.2.3`
