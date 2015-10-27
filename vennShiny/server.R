library(shiny)

# Define server logic required to draw a Venn's plot
shinyServer(function(input, output) {

    kindvennInput <- reactive({
        switch(input$kindvenn,
               "simple"=funct1,
               "proportional"=funct2,
               "network"=funct3)
    })
    output$vennPlot <- renderPlot({
        # data
        # property of the graph
        # draw the plot
    })
})

