def convert_input(description):
    return """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?card ?cardHeader ?title ?subtitle ?grid ?row ?col WHERE {
          ?card rdf:type ?Ion_Element.
          ?card ?contains ?cardHeader.
          ?cardHeader rdf:type ?Ion_Card_Header.
          ?cardHeader ?contains ?title.
          ?title rdf:type ?Ion_Card_Title.
          ?cardHeader ?contains ?subtitle.
          ?subtitle rdf:type ?Ion_Card_Subtitle.
          ?card ?contains ?grid.
          ?grid rdf:type ?Ion_Grid.
        } LIMIT 1
    """
