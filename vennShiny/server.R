library(shiny)

# Define server logic required to draw a Venn's plot
shinyServer(function(input, output) {
  kindOfVenn <- reactive({
    switch(input$venntype,
           "simple" = "simple",
           "proportional" = "proportional",
           "bvenn" = "bvenn")
  })

  output$choice <- renderPrint({
    kOV <- kindOfVenn()
    (kOV)
  })

})

