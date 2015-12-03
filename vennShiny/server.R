library(shiny)

# Define server logic required to draw a Venn's plot
shinyServer(function(input, output) {
  kindOfVenn <- reactive({
    switch(input$venntype,
           "simple" = "simple",
           "proportional" = "proportional",
           "bvenn" = "bvenn")
  })

  output$contents <- renderTable({
    
    # input$file1 will be NULL initially. After the user selects
    # and uploads a file, it will be a data frame with 'name',
    # 'size', 'type', and 'datapath' columns. The 'datapath'
    # column will contain the local filenames where the data can
    # be found.

    inFile <- input$file1

    if (is.null(inFile))
      return(NULL)
    
    read.csv(inFile$datapath, header=input$header, sep=input$sep, 
                 quote=input$quote)
  })

  output$choice <- renderPrint({
    kOV <- kindOfVenn()
    (kOV)
  })

})

