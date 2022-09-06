# extractive_summarize
extractive summarization with clustering and sentence embeddings


SETUP STEPS: 
```

1. cd extractive_summarize/
2. pip install -r req.txt
3. pip install "uvicorn[standard]" gunicorn
```
once installed run the following, make sure port open for the vm or port forward (for eg. with vscode)

```
uvicorn app.main:app --host 0.0.0.0 --port 8080

```
Go to the url and try out the summaraize url
```
http://<YOUR_HOST_IP>:8080/v1/docs
```

DOCS page will have pre-filled input to try the example, also find below the sample input and response

```
{
  "request_id": "123",
  "text": "The Chrysler Building, the famous art deco New York skyscraper, will be sold for a small fraction of its previous sales price.\n    The deal, first reported by The Real Deal, was for $150 million, according to a source familiar with the deal.\n    Mubadala, an Abu Dhabi investment fund, purchased 90 percent of the building for $800 million in 2008.\n    Real estate firm Tishman Speyer had owned the other 10%.\n    The buyer is RFR Holding, a New York real estate company.\n    Officials with Tishman and RFR did not immediately respond to a request for comments.\n    It's unclear when the deal will close.\n    The building sold fairly quickly after being publicly placed on the market only two months ago.\n    The sale was handled by CBRE Group.\n    The incentive to sell the building at such a huge loss was due to the soaring rent the owners pay to Cooper Union, a New York college, for the land under the building.\n    The rent is rising from $7.75 million last year to $32.5 million this year to $41 million in 2028.\n    Meantime, rents in the building itself are not rising nearly that fast.\n    While the building is an iconic landmark in the New York skyline, it is competing against newer office towers with large floor-to-ceiling windows and all the modern amenities.\n    Still the building is among the best known in the city, even to people who have never been to New York.\n    It is famous for its triangle-shaped, vaulted windows worked into the stylized crown, along with its distinctive eagle gargoyles near the top.\n    It has been featured prominently in many films, including Men in Black 3, Spider-Man, Armageddon, Two Weeks Notice and Independence Day.\n    The previous sale took place just before the 2008 financial meltdown led to a plunge in real estate prices.\n    Still there have been a number of high profile skyscrapers purchased for top dollar in recent years, including the Waldorf Astoria hotel, which Chinese firm Anbang Insurance purchased in 2016 for nearly $2 billion, and the Willis Tower in Chicago, which was formerly known as Sears Tower, once the world's tallest.\n    Blackstone Group (BX) bought it for $1.3 billion 2015.\n    The Chrysler Building was the headquarters of the American automaker until 1953, but it was named for and owned by Chrysler chief Walter Chrysler, not the company itself.\n    Walter Chrysler had set out to build the tallest building in the world, a competition at that time with another Manhattan skyscraper under construction at 40 Wall Street at the south end of Manhattan. He kept secret the plans for the spire that would grace the top of the building, building it inside the structure and out of view of the public until 40 Wall Street was complete.\n    Once the competitor could rise no higher, the spire of the Chrysler building was raised into view, giving it the title.\n"
}
```

Response:

```
{
  "status": true,
  "summarized_text": "The Chrysler Building, the famous art deco New York skyscraper, will be sold for a small fraction of its previous sales price. The deal, first reported by The Real Deal, was for $150 million, according to a source familiar with the deal. The incentive to sell the building at such a huge loss was due to the soaring rent the owners pay to Cooper Union, a New York college, for the land under the building. Meantime, rents in the building itself are not rising nearly that fast. Still there have been a number of high profile skyscrapers purchased for top dollar in recent years, including the Waldorf Astoria hotel, which Chinese firm Anbang Insurance purchased in 2016 for nearly $2 billion, and the Willis Tower in Chicago, which was formerly known as Sears Tower, once the world's tallest."
}
```
