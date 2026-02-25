We use these APIs in the workflow:
FMP: Financial data (I have a paid subscription so this should always be the default for financial data unless there is something it doesn't have/something is on a higher paid tier, in which case Alphavantage is probably the best option). 
Alphavantage: Financial data. Limited to 25 requests per day on free tier. 
Perigon: News. limited to 150 requests per month on free tier. 
SociaVault: Social media (i have paid for many credits from sociavault so we can use this one liberally). 

We use these APIs in the workflow:
FMP: Financial data (I have a paid subscription so this should always be the default for financial data unless there is something it doesn't have/something is on a higher paid tier, in which case Alphavantage is probably the best option). 
Alphavantage: Financial data. Limited to 25 requests per day on free tier. 
Perigon: News. limited to 150 requests per month on free tier. 
SociaVault: Social media (i have paid for many credits from sociavault so we can use this one liberally). 

# FMP:

## Company Search
* Stock Symbol Search API: Easily find the ticker symbol of any stock with the FMP Stock Symbol Search API. Search by symbol across multiple global markets.
* Company Name Search API: Search for ticker symbols, company names, and exchange details for equity securities and ETFs listed on various exchanges with the FMP Name Search API. This endpoint is useful for retrieving ticker symbols when you know the full or partial company or asset name but not the symbol identifier.
* CIK API: Easily retrieve the Central Index Key (CIK) for publicly traded companies with the FMP CIK API. Access unique identifiers needed for SEC filings and regulatory documents for a streamlined compliance and financial analysis process.
* CUSIP API: Easily search and retrieve financial securities information by CUSIP number using the FMP CUSIP API. Find key details such as company name, stock symbol, and market capitalization associated with the CUSIP.
* ISIN API: Easily search and retrieve the International Securities Identification Number (ISIN) for financial securities using the FMP ISIN API. Find key details such as company name, stock symbol, and market capitalization associated with the ISIN.
* Stock Screener API: Discover stocks that align with your investment strategy using the FMP Stock Screener API. Filter stocks based on market cap, price, volume, beta, sector, country, and more to identify the best opportunities.
* Exchange Variants API: Search across multiple public exchanges to find where a given stock symbol is listed using the FMP Exchange Variants API. This allows users to quickly identify all the exchanges where a security is actively traded.

## Stock Directory
* Company Symbols List API: Easily retrieve a comprehensive list of financial symbols with the FMP Company Symbols List API. Access a broad range of stock symbols and other tradable financial instruments from various global exchanges, helping you explore the full range of available securities.
* Financial Statement Symbols List API: Access a comprehensive list of companies with available financial statements through the FMP Financial Statement Symbols List API. Find companies listed on major global exchanges and obtain up-to-date financial data including income statements, balance sheets, and cash flow statements, are provided.
* CIK List API: Access a comprehensive database of CIK (Central Index Key) numbers for SEC-registered entities with the FMP CIK List API. This endpoint is essential for businesses, financial professionals, and individuals who need quick access to CIK numbers for regulatory compliance, financial transactions, and investment research.
* Symbol Changes List API: Stay informed about the latest stock symbol changes with the FMP Stock Symbol Changes API. Track changes due to mergers, acquisitions, stock splits, and name changes to ensure accurate trading and analysis.
* ETF Symbol Search API: Quickly find ticker symbols and company names for Exchange Traded Funds (ETFs) using the FMP ETF Symbol Search API. This tool simplifies identifying specific ETFs by their name or ticker.
* Actively Trading List API: List all actively trading companies and financial instruments with the FMP Actively Trading List API. This endpoint allows users to filter and display securities that are currently being traded on public exchanges, ensuring you access real-time market activity.
* Earnings Transcript List API: Access available earnings transcripts for companies with the FMP Earnings Transcript List API. Retrieve a list of companies with earnings transcripts, along with the total number of transcripts available for each company.
* Available Exchanges API: Access a complete list of supported stock exchanges using the FMP Available Exchanges API. This API provides a comprehensive overview of global stock exchanges, allowing users to identify where securities are traded and filter data by specific exchanges for further analysis.
* Available Sectors API: Access a complete list of industry sectors using the FMP Available Sectors API. This API helps users categorize and filter companies based on their respective sectors, enabling deeper analysis and more focused queries across different industries.
* Available Industries API: Access a comprehensive list of industries where stock symbols are available using the FMP Available Industries API. This API helps users filter and categorize companies based on their industry for more focused research and analysis.
* Available Countries API: Access a comprehensive list of countries where stock symbols are available with the FMP Available Countries API. This API enables users to filter and analyze stock symbols based on the country of origin or the primary market where the securities are traded.

## Company Information
* Company Profile Data API: Access detailed company profile data with the FMP Company Profile Data API. This API provides key financial and operational information for a specific stock symbol, including the company's market capitalization, stock price, industry, and much more.
* Company Profile by CIK API: Retrieve detailed company profile data by CIK (Central Index Key) with the FMP Company Profile by CIK API. This API allows users to search for companies using their unique CIK identifier and access a full range of company data, including stock price, market capitalization, industry, and much more.
* Company Notes API: Retrieve detailed information about company-issued notes with the FMP Company Notes API. Access essential data such as CIK number, stock symbol, note title, and the exchange where the notes are listed.
* Stock Peer Comparison API: Identify and compare companies within the same sector and market capitalization range using the FMP Stock Peer Comparison API. Gain insights into how a company stacks up against its peers on the same exchange.
* Delisted Companies API: Stay informed with the FMP Delisted Companies API. Access a comprehensive list of companies that have been delisted from US exchanges to avoid trading in risky stocks and identify potential financial troubles.
* Company Employee Count API: Retrieve detailed workforce information for companies, including employee count, reporting period, and filing date. The FMP Company Employee Count API also provides direct links to official SEC documents for further verification and in-depth research.
* Company Historical Employee Count API: Access historical employee count data for a company based on specific reporting periods. The FMP Company Historical Employee Count API provides insights into how a company’s workforce has evolved over time, allowing users to analyze growth trends and operational changes.
* Company Market Cap API: Retrieve the market capitalization for a specific company on any given date using the FMP Company Market Capitalization API. This API provides essential data to assess the size and value of a company in the stock market, helping users gauge its overall market standing.
* Batch Market Cap API: Retrieve market capitalization data for multiple companies in a single request with the FMP Batch Market Capitalization API. This API allows users to compare the market size of various companies simultaneously, streamlining the analysis of company valuations.
* Historical Market Cap API: Access historical market capitalization data for a company using the FMP Historical Market Capitalization API. This API helps track the changes in market value over time, enabling long-term assessments of a company's growth or decline.
* Company Share Float & Liquidity API: Understand the liquidity and volatility of a stock with the FMP Company Share Float and Liquidity API. Access the total number of publicly traded shares for any company to make informed investment decisions.
* All Shares Float API: Access comprehensive shares float data for all available companies with the FMP All Shares Float API. Retrieve critical information such as free float, float shares, and outstanding shares to analyze liquidity across a wide range of companies.
* Latest Mergers & Acquisitions API: Access real-time data on the latest mergers and acquisitions with the FMP Latest Mergers and Acquisitions API. This API provides key information such as the transaction date, company names, and links to detailed filing information for further analysis.
* Search Mergers & Acquisitions API: Search for specific mergers and acquisitions data with the FMP Search Mergers and Acquisitions API. Retrieve detailed information on M&A activity, including acquiring and targeted companies, transaction dates, and links to official SEC filings.
* Company Executives API: Retrieve detailed information on company executives with the FMP Company Executives API. This API provides essential data about key executives, including their name, title, compensation, and other demographic details such as gender and year of birth.
* Executive Compensation API: Retrieve comprehensive compensation data for company executives with the FMP Executive Compensation API. This API provides detailed information on salaries, stock awards, total compensation, and other relevant financial data, including filing details and links to official documents.
* Executive Compensation Benchmark API: Gain access to average executive compensation data across various industries with the FMP Executive Compensation Benchmark API. This API provides essential insights for comparing executive pay by industry, helping you understand compensation trends and benchmarks.

## Quote
* Stock Quote API: Access real-time stock quotes with the FMP Stock Quote API. Get up-to-the-minute prices, changes, and volume data for individual stocks.
* Stock Quote Short API: Get quick snapshots of real-time stock quotes with the FMP Stock Quote Short API. Access key stock data like current price, volume, and price changes for instant market insights.
* Aftermarket Trade API: Track real-time trading activity occurring after regular market hours with the FMP Aftermarket Trade API. Access key details such as trade prices, sizes, and timestamps for trades executed during the post-market session.
* Aftermarket Quote API: Access real-time aftermarket quotes for stocks with the FMP Aftermarket Quote API. Track bid and ask prices, volume, and other relevant data outside of regular trading hours.
* Stock Price Change API: Track stock price fluctuations in real-time with the FMP Stock Price Change API. Monitor percentage and value changes over various time periods, including daily, weekly, monthly, and long-term.
* Stock Batch Quote API: Retrieve multiple real-time stock quotes in a single request with the FMP Stock Batch Quote API. Access current prices, volume, and detailed data for multiple companies at once, making it easier to track large portfolios or monitor multiple stocks simultaneously.
* Stock Batch Quote Short API: Access real-time, short-form quotes for multiple stocks with the FMP Stock Batch Quote Short API. Get a quick snapshot of key stock data such as current price, change, and volume for several companies in one streamlined request.
* Batch Aftermarket Trade API: Retrieve real-time aftermarket trading data for multiple stocks with the FMP Batch Aftermarket Trade API. Track post-market trade prices, volumes, and timestamps across several companies simultaneously.
* Batch Aftermarket Quote API: Retrieve real-time aftermarket quotes for multiple stocks with the FMP Batch Aftermarket Quote API. Access bid and ask prices, volume, and other relevant data for several companies during post-market trading.
* Exchange Stock Quotes API: Retrieve real-time stock quotes for all listed stocks on a specific exchange with the FMP Exchange Stock Quotes API. Track price changes and trading activity across the entire exchange.
* Mutual Fund Price Quotes API: Access real-time quotes for mutual funds with the FMP Mutual Fund Price Quotes API. Track current prices, performance changes, and key data for various mutual funds.
* ETF Price Quotes API: Get real-time price quotes for exchange-traded funds (ETFs) with the FMP ETF Price Quotes API. Track current prices, performance changes, and key data for a wide variety of ETFs.
* Full Commodities Quotes API: Get up-to-the-minute quotes for commodities with the FMP Real-Time Commodities Quotes API. Track the latest prices, changes, and volumes for a wide range of commodities, including oil, gold, and agricultural products.
* Full Cryptocurrency Quotes API: Access real-time cryptocurrency quotes with the FMP Full Cryptocurrency Quotes API. Track live prices, trading volumes, and price changes for a wide range of digital assets.
* Full Forex Quote API: Retrieve real-time quotes for multiple forex currency pairs with the FMP Batch Forex Quote API. Get real-time price changes and updates for a variety of forex pairs in a single request.
* Full Index Quotes API: Track real-time movements of major stock market indexes with the FMP Stock Market Index Quotes API. Access live quotes for global indexes and monitor changes in their performance.

## Statements
* Income Statement API: Access detailed income statement data for publicly traded companies with the Income Statements API. Track profitability, compare competitors, and identify business trends with up-to-date financial data.
* Balance Sheet Statement API: Access detailed balance sheet statements for publicly traded companies with the Balance Sheet Data API. Analyze assets, liabilities, and shareholder equity to gain insights into a company's financial health.
* Cash Flow Statement API: Gain insights into a company's cash flow activities with the Cash Flow Statements API. Analyze cash generated and used from operations, investments, and financing activities to evaluate the financial health and sustainability of a business.
* Latest Financial Statements API: 
* Income Statements TTM API: 
* Balance Sheet Statements TTM API: 
* Cashflow Statements TTM API: 
* Key Metrics API: Access essential financial metrics for a company with the FMP Financial Key Metrics API. Evaluate revenue, net income, P/E ratio, and more to assess performance and compare it to competitors.
* Financial Ratios API: Analyze a company's financial performance using the Financial Ratios API. This API provides detailed profitability, liquidity, and efficiency ratios, enabling users to assess a company's operational and financial health across various metrics.
* Key Metrics TTM API: Retrieve a comprehensive set of trailing twelve-month (TTM) key performance metrics with the TTM Key Metrics API. Access data related to a company's profitability, capital efficiency, and liquidity, allowing for detailed analysis of its financial health over the past year.
* Financial Ratios TTM API: Gain access to trailing twelve-month (TTM) financial ratios with the TTM Ratios API. This API provides key performance metrics over the past year, including profitability, liquidity, and efficiency ratios.
* Financial Scores API: Assess a company's financial strength using the Financial Health Scores API. This API provides key metrics such as the Altman Z-Score and Piotroski Score, giving users insights into a company’s overall financial health and stability.
* Owner Earnings API: Retrieve a company's owner earnings with the Owner Earnings API, which provides a more accurate representation of cash available to shareholders by adjusting net income. This metric is crucial for evaluating a company’s profitability from the perspective of investors.
* Enterprise Values API: Access a company's enterprise value using the Enterprise Values API. This metric offers a comprehensive view of a company's total market value by combining both its equity (market capitalization) and debt, providing a better understanding of its worth.
* Income Statement Growth API: Track key financial growth metrics with the Income Statement Growth API. Analyze how revenue, profits, and expenses have evolved over time, offering insights into a company’s financial health and operational efficiency.
* Balance Sheet Statement Growth API: Analyze the growth of key balance sheet items over time with the Balance Sheet Statement Growth API. Track changes in assets, liabilities, and equity to understand the financial evolution of a company.
* Cashflow Statement Growth API: Measure the growth rate of a company’s cash flow with the FMP Cashflow Statement Growth API. Determine how quickly a company’s cash flow is increasing or decreasing over time.
* Financial Statement Growth API: Analyze the growth of key financial statement items across income, balance sheet, and cash flow statements with the Financial Statement Growth API. Track changes over time to understand trends in financial performance.
* Financial Reports Dates API: 
* Financial Reports Form 10-K JSON API: Access comprehensive annual reports with the FMP Annual Reports on Form 10-K API. Obtain detailed information about a company’s financial performance, business operations, and risk factors as reported to the SEC.
* Financial Reports Form 10-K XLSX API: Download detailed 10-K reports in XLSX format with the Financial Reports Form 10-K XLSX API. Effortlessly access and analyze annual financial data for companies in a spreadsheet-friendly format.
* Revenue Product Segmentation API: Access detailed revenue breakdowns by product line with the Revenue Product Segmentation API. Understand which products drive a company's earnings and get insights into the performance of individual product segments.
* Revenue Geographic Segments API: Access detailed revenue breakdowns by geographic region with the Revenue Geographic Segments API. Analyze how different regions contribute to a company’s total revenue and identify key markets for growth.
* As Reported Income Statements API: Retrieve income statements as they were reported by the company with the As Reported Income Statements API. Access raw financial data directly from official company filings, including revenue, expenses, and net income.
* As Reported Balance Statements API: Access balance sheets as reported by the company with the As Reported Balance Statements API. View detailed financial data on assets, liabilities, and equity directly from official filings.
* As Reported Cashflow Statements API: View cash flow statements as reported by the company with the As Reported Cash Flow Statements API. Analyze a company's cash flows related to operations, investments, and financing directly from official reports.
* As Reported Financial Statements API: Retrieve comprehensive financial statements as reported by companies with FMP As Reported Financial Statements API. Access complete data across income, balance sheet, and cash flow statements in their original form for detailed analysis.

## Charts
* Stock Chart Light API: Access simplified stock chart data using the FMP Basic Stock Chart API. This API provides essential charting information, including date, price, and trading volume, making it ideal for tracking stock performance with minimal data and creating basic price and volume charts.
* Stock Price and Volume Data API: Access full price and volume data for any stock symbol using the FMP Comprehensive Stock Price and Volume Data API. Get detailed insights, including open, high, low, close prices, trading volume, price changes, percentage changes, and volume-weighted average price (VWAP).
* Unadjusted Stock Price API: Access stock price and volume data without adjustments for stock splits with the FMP Unadjusted Stock Price Chart API. Get accurate insights into stock performance, including open, high, low, and close prices, along with trading volume, without split-related changes.
* Dividend Adjusted Price Chart API: Analyze stock performance with dividend adjustments using the FMP Dividend-Adjusted Price Chart API. Access end-of-day price and volume data that accounts for dividend payouts, offering a more comprehensive view of stock trends over time.
* 1 Min Interval Stock Chart API: Access precise intraday stock price and volume data with the FMP 1-Minute Interval Stock Chart API. Retrieve real-time or historical stock data in 1-minute intervals, including key information such as open, high, low, and close prices, and trading volume for each minute.
* 5 Min Interval Stock Chart API: Access stock price and volume data with the FMP 5-Minute Interval Stock Chart API. Retrieve detailed stock data in 5-minute intervals, including open, high, low, and close prices, along with trading volume for each 5-minute period. This API is perfect for short-term trading analysis and building intraday charts.
* 15 Min Interval Stock Chart API: Access stock price and volume data with the FMP 15-Minute Interval Stock Chart API. Retrieve detailed stock data in 15-minute intervals, including open, high, low, close prices, and trading volume. This API is ideal for creating intraday charts and analyzing medium-term price trends during the trading day.
* 30 Min Interval Stock Chart API: Access stock price and volume data with the FMP 30-Minute Interval Stock Chart API. Retrieve essential stock data in 30-minute intervals, including open, high, low, close prices, and trading volume. This API is perfect for creating intraday charts and tracking medium-term price movements for more strategic trading decisions.
* 1 Hour Interval Stock Chart API: Track stock price movements over hourly intervals with the FMP 1-Hour Interval Stock Chart API. Access essential stock price and volume data, including open, high, low, and close prices for each hour, to analyze broader intraday trends with precision.
* 4 Hour Interval Stock Chart API: Analyze stock price movements over extended intraday periods with the FMP 4-Hour Interval Stock Chart API. Access key stock price and volume data in 4-hour intervals, perfect for tracking longer intraday trends and understanding broader market movements.

## Economics
* Treasury Rates API: Access latest and historical Treasury rates for all maturities with the FMP Treasury Rates API. Track key benchmarks for interest rates across the economy.
* Economics Indicators API: Access real-time and historical economic data for key indicators like GDP, unemployment, and inflation with the FMP Economic Indicators API. Use this data to measure economic performance and identify growth trends.
* Economic Data Releases Calendar API: Stay informed with the FMP Economic Data Releases Calendar API. Access a comprehensive calendar of upcoming economic data releases to prepare for market impacts and make informed investment decisions.
* Market Risk Premium API: Access the market risk premium for specific dates with the FMP Market Risk Premium API. Use this key financial metric to assess the additional return expected from investing in the stock market over a risk-free investment.

## Earnings, Dividends, Splits
* Dividends Company API: Stay informed about upcoming dividend payments with the FMP Dividends Company API. This API provides essential dividend data for individual stock symbols, including record dates, payment dates, declaration dates, and more.
* Dividends Calendar API: Stay informed on upcoming dividend events with the Dividend Events Calendar API. Access a comprehensive schedule of dividend-related dates for all stocks, including record dates, payment dates, declaration dates, and dividend yields.
* Earnings Report API: Retrieve in-depth earnings information with the FMP Earnings Report API. Gain access to key financial data for a specific stock symbol, including earnings report dates, EPS estimates, and revenue projections to help you stay on top of company performance.
* Earnings Calendar API: Stay informed on upcoming and past earnings announcements with the FMP Earnings Calendar API. Access key data, including announcement dates, estimated earnings per share (EPS), and actual EPS for publicly traded companies.
* IPOs Calendar API: Access a comprehensive list of all upcoming initial public offerings (IPOs) with the FMP IPO Calendar API. Stay up to date on the latest companies entering the public market, with essential details on IPO dates, company names, expected pricing, and exchange listings.
* IPOs Disclosure API: Access a comprehensive list of disclosure filings for upcoming initial public offerings (IPOs) with the FMP IPO Disclosures API. Stay updated on regulatory filings, including filing dates, effectiveness dates, CIK numbers, and form types, with direct links to official SEC documents.
* IPOs Prospectus API: Access comprehensive information on IPO prospectuses with the FMP IPO Prospectus API. Get key financial details, such as public offering prices, discounts, commissions, proceeds before expenses, and more. This API also provides links to official SEC prospectuses, helping investors stay informed on companies entering the public market.
* Stock Split Details API: Access detailed information on stock splits for a specific company using the FMP Stock Split Details API. This API provides essential data, including the split date and the split ratio, helping users understand changes in a company's share structure after a stock split.
* Stock Splits Calendar API: Stay informed about upcoming stock splits with the FMP Stock Splits Calendar API. This API provides essential data on upcoming stock splits across multiple companies, including the split date and ratio, helping you track changes in share structures before they occur.

## Earnings Transcript
* Latest Earning Transcripts API: Access available earnings transcripts for companies with the FMP Latest Earning Transcripts API. Retrieve a list of companies with earnings transcripts, along with the total number of transcripts available for each company.
* Earnings Transcript API: Access the full transcript of a company’s earnings call with the FMP Earnings Transcript API. Stay informed about a company’s financial performance, future plans, and overall strategy by analyzing management's communication.
* Transcripts Dates By Symbol API: Access earnings call transcript dates for specific companies with the FMP Transcripts Dates By Symbol API. Get a comprehensive overview of earnings call schedules based on fiscal year and quarter.
* Available Transcript Symbols API: Access a complete list of stock symbols with available earnings call transcripts using the FMP Available Earnings Transcript Symbols API. Retrieve information on which companies have earnings transcripts and how many are accessible for detailed financial analysis.

## News
* FMP Articles API: Access the latest articles from Financial Modeling Prep with the FMP Articles API. Get comprehensive updates including headlines, snippets, and publication URLs.
* General News API: Access the latest general news articles from a variety of sources with the FMP General News API. Obtain headlines, snippets, and publication URLs for comprehensive news coverage.
* Press Releases API: Access official company press releases with the FMP Press Releases API. Get real-time updates on corporate announcements, earnings reports, mergers, and more.
* Stock News API: Stay informed with the latest stock market news using the FMP Stock News Feed API. Access headlines, snippets, publication URLs, and ticker symbols for the most recent articles from a variety of sources.
* Crypto News API: Stay informed with the latest cryptocurrency news using the FMP Crypto News API. Access a curated list of articles from various sources, including headlines, snippets, and publication URLs.
* Forex News API: Stay updated with the latest forex news articles from various sources using the FMP Forex News API. Access headlines, snippets, and publication URLs for comprehensive market insights.
* Search Press Releases API: Search for company press releases with the FMP Search Press Releases API. Find specific corporate announcements and updates by entering a stock symbol or company name.
* Search Stock News API: Search for stock-related news using the FMP Search Stock News API. Find specific stock news by entering a ticker symbol or company name to track the latest developments.
* Search Crypto News API: Search for cryptocurrency news using the FMP Search Crypto News API. Retrieve news related to specific coins or tokens by entering their name or symbol.
* Search Forex News API: Search for foreign exchange news using the FMP Search Forex News API. Find targeted news on specific currency pairs by entering their symbols for focused updates.

## Form 13F
* Institutional Ownership Filings API: Stay up to date with the most recent SEC filings related to institutional ownership using the Institutional Ownership Filings API. This tool allows you to track the latest reports and disclosures from institutional investors, giving you a real-time view of major holdings and regulatory submissions.
* Filings Extract API: The SEC Filings Extract API allows users to extract detailed data directly from official SEC filings. This API provides access to key information such as company shares, security details, and filing links, making it easier to analyze corporate disclosures.
* Form 13F Filings Dates API: The Form 13F Filings Dates API allows you to retrieve dates associated with Form 13F filings by institutional investors. This is crucial for tracking stock holdings of institutional investors at specific points in time, providing valuable insights into their investment strategies.
* Filings Extract With Analytics By Holder API: The Filings Extract With Analytics By Holder API provides an analytical breakdown of institutional filings. This API offers insight into stock movements, strategies, and portfolio changes by major institutional holders, helping you understand their investment behavior and track significant changes in stock ownership.
* Holder Performance Summary API: The Holder Performance Summary API provides insights into the performance of institutional investors based on their stock holdings. This data helps track how well institutional holders are performing, their portfolio changes, and how their performance compares to benchmarks like the S&P 500.
* Holders Industry Breakdown API: The Holders Industry Breakdown API provides an overview of the sectors and industries that institutional holders are investing in. This API helps analyze how institutional investors distribute their holdings across different industries and track changes in their investment strategies over time.
* Positions Summary API: The Positions Summary API provides a comprehensive snapshot of institutional holdings for a specific stock symbol. It tracks key metrics like the number of investors holding the stock, changes in the number of shares, total investment value, and ownership percentages over time.
* Industry Performance Summary API: The Industry Performance Summary API provides an overview of how various industries are performing financially. By analyzing the value of industries over a specific period, this API helps investors and analysts understand the health of entire sectors and make informed decisions about sector-based investments.

## Analyst
* Financial Estimates API: Retrieve analyst financial estimates for stock symbols with the FMP Financial Estimates API. Access projected figures like revenue, earnings per share (EPS), and other key financial metrics as forecasted by industry analysts to inform your investment decisions.
* Ratings Snapshot API: Quickly assess the financial health and performance of companies with the FMP Ratings Snapshot API. This API provides a comprehensive snapshot of financial ratings for stock symbols in our database, based on various key financial ratios.
* Historical Ratings API: Track changes in financial performance over time with the FMP Historical Ratings API. This API provides access to historical financial ratings for stock symbols in our database, allowing users to view ratings and key financial metric scores for specific dates.
* Price Target Summary API: Gain insights into analysts' expectations for stock prices with the FMP Price Target Summary API. This API provides access to average price targets from analysts across various timeframes, helping investors assess future stock performance based on expert opinions.
* Price Target Consensus API: Access analysts' consensus price targets with the FMP Price Target Consensus API. This API provides high, low, median, and consensus price targets for stocks, offering investors a comprehensive view of market expectations for future stock prices.
* Stock Grades API: Access the latest stock grades from top analysts and financial institutions with the FMP Grades API. Track grading actions, such as upgrades, downgrades, or maintained ratings, for specific stock symbols, providing valuable insight into how experts evaluate companies over time.
* Historical Stock Grades API: Access a comprehensive record of analyst grades with the FMP Historical Grades API. This tool allows you to track historical changes in analyst ratings for specific stock symbol
* Stock Grades Summary API: Quickly access an overall view of analyst ratings with the FMP Grades Summary API. This API provides a consolidated summary of market sentiment for individual stock symbols, including the total number of strong buy, buy, hold, sell, and strong sell ratings. Understand the overall consensus on a stock’s outlook with just a few data points.

## Market Performance
* Market Sector Performance Snapshot API: Get a snapshot of sector performance using the Market Sector Performance Snapshot API. Analyze how different industries are performing in the market based on average changes across sectors.
* Industry Performance Snapshot API: Access detailed performance data by industry using the Industry Performance Snapshot API. Analyze trends, movements, and daily performance metrics for specific industries across various stock exchanges.
* Historical Market Sector Performance API: Access historical sector performance data using the Historical Market Sector Performance API. Review how different sectors have performed over time across various stock exchanges.
* Historical Industry Performance API: Access historical performance data for industries using the Historical Industry Performance API. Track long-term trends and analyze how different industries have evolved over time across various stock exchanges.
* Sector PE Snapshot API: Retrieve the price-to-earnings (P/E) ratios for various sectors using the Sector P/E Snapshot API. Compare valuation levels across sectors to better understand market valuations.
* Industry PE Snapshot API: View price-to-earnings (P/E) ratios for different industries using the Industry P/E Snapshot API. Analyze valuation levels across various industries to understand how each is priced relative to its earnings.
* Historical Sector PE API: Access historical price-to-earnings (P/E) ratios for various sectors using the Historical Sector P/E API. Analyze how sector valuations have evolved over time to understand long-term trends and market shifts.
* Historical Industry PE API: Access historical price-to-earnings (P/E) ratios by industry using the Historical Industry P/E API. Track valuation trends across various industries to understand how market sentiment and valuations have evolved over time.
* Biggest Stock Gainers API: Track the stocks with the largest price increases using the Top Stock Gainers API. Identify the companies that are leading the market with significant price surges, offering potential growth opportunities.
* Biggest Stock Losers API: Access data on the stocks with the largest price drops using the Biggest Stock Losers API. Identify companies experiencing significant declines and track the stocks that are falling the fastest in the market.
* Top Traded Stocks API: View the most actively traded stocks using the Top Traded Stocks API. Identify the companies experiencing the highest trading volumes in the market and track where the most trading activity is happening.

## Technical Indicators
* Simple Moving Average API: 
* Exponential Moving Average API: 
* Weighted Moving Average API: 
* Double Exponential Moving Average API: 
* Triple Exponential Moving Average API: 
* Relative Strength Index API: 
* Standard Deviation API: 
* Williams API: 
* Average Directional Index API: 

## Etf And Mutual Funds
* ETF & Fund Holdings API: Get a detailed breakdown of the assets held within ETFs and mutual funds using the FMP ETF & Fund Holdings API. Access real-time data on the specific securities and their weights in the portfolio, providing insights into asset composition and fund strategies.
* ETF & Mutual Fund Information API: Access comprehensive data on ETFs and mutual funds with the FMP ETF & Mutual Fund Information API. Retrieve essential details such as ticker symbol, fund name, expense ratio, assets under management, and more.
* ETF & Fund Country Allocation API: Gain insight into how ETFs and mutual funds distribute assets across different countries with the FMP ETF & Fund Country Allocation API. This tool provides detailed information on the percentage of assets allocated to various regions, helping you make informed investment decisions.
* ETF Asset Exposure API: Discover which ETFs hold specific stocks with the FMP ETF Asset Exposure API. Access detailed information on market value, share numbers, and weight percentages for assets within ETFs.
* ETF Sector Weighting API: The FMP ETF Sector Weighting API provides a breakdown of the percentage of an ETF's assets that are invested in each sector. For example, an investor may want to invest in an ETF that has a high exposure to the technology sector if they believe that the technology sector is poised for growth.
* Mutual Fund & ETF Disclosure API: Access the latest disclosures from mutual funds and ETFs with the FMP Mutual Fund & ETF Disclosure API. This API provides updates on filings, changes in holdings, and other critical disclosure data for mutual funds and ETFs.
* Mutual Fund Disclosures API: Access comprehensive disclosure data for mutual funds with the FMP Mutual Fund Disclosures API. Analyze recent filings, balance sheets, and financial reports to gain insights into mutual fund portfolios.
* Mutual Fund & ETF Disclosure Name Search API: Easily search for mutual fund and ETF disclosures by name using the Mutual Fund & ETF Disclosure Name Search API. This API allows you to find specific reports and filings based on the fund or ETF name, providing essential details like CIK number, entity information, and reporting file number.
* Fund & ETF Disclosures by Date API: Retrieve detailed disclosures for mutual funds and ETFs based on filing dates with the FMP Fund & ETF Disclosures by Date API. Stay current with the latest filings and track regulatory updates effectively.

## Sec Filings
* Latest 8-K SEC Filings API: Stay up-to-date with the most recent 8-K filings from publicly traded companies using the FMP Latest 8-K SEC Filings API. Get real-time access to significant company events such as mergers, acquisitions, leadership changes, and other material events that may impact the market.
* Latest SEC Filings API: Stay updated with the most recent SEC filings from publicly traded companies using the FMP Latest SEC Filings API. Access essential regulatory documents, including financial statements, annual reports, 8-K, 10-K, and 10-Q forms.
* SEC Filings By Form Type API: Search for specific SEC filings by form type with the FMP SEC Filings By Form Type API. Retrieve filings such as 10-K, 10-Q, 8-K, and others, filtered by the exact type of document you're looking for.
* SEC Filings By Symbol API: Search and retrieve SEC filings by company symbol using the FMP SEC Filings By Symbol API. Gain direct access to regulatory filings such as 8-K, 10-K, and 10-Q reports for publicly traded companies.
* SEC Filings By CIK API: Search for SEC filings using the FMP SEC Filings By CIK API. Access detailed regulatory filings by Central Index Key (CIK) number, enabling you to track all filings related to a specific company or entity.
* SEC Filings By Name API: Search for SEC filings by company or entity name using the FMP SEC Filings By Name API. Quickly retrieve official filings for any organization based on its name.
* SEC Filings Company Search By Symbol API: Find company information and regulatory filings using a stock symbol with the FMP SEC Filings Company Search By Symbol API. Quickly access essential company details based on stock ticker symbols.
* SEC Filings Company Search By CIK API: Easily find company information using a CIK (Central Index Key) with the FMP SEC Filings Company Search By CIK API. Access essential company details and filings linked to a specific CIK number.
* SEC Company Full Profile API: Retrieve detailed company profiles, including business descriptions, executive details, contact information, and financial data with the FMP SEC Company Full Profile API.
* Industry Classification List API: Retrieve a comprehensive list of industry classifications, including Standard Industrial Classification (SIC) codes and industry titles with the FMP Industry Classification List API.
* Industry Classification Search API: Search and retrieve industry classification details for companies, including SIC codes, industry titles, and business information, with the FMP Industry Classification Search API.
* All Industry Classification API: Access comprehensive industry classification data for companies across all sectors with the FMP All Industry Classification API. Retrieve key details such as SIC codes, industry titles, and business contact information.

## Insider Trades
* Latest Insider Trading API: Access the latest insider trading activity using the Latest Insider Trading API. Track which company insiders are buying or selling stocks and analyze their transactions.
* Search Insider Trades API: Search insider trading activity by company or symbol using the Search Insider Trades API. Find specific trades made by corporate insiders, including executives and directors.
* Search Insider Trades by Reporting Name API: Search for insider trading activity by reporting name using the Search Insider Trades by Reporting Name API. Track trading activities of specific individuals or groups involved in corporate insider transactions.
* All Insider Transaction Types API: Access a comprehensive list of insider transaction types with the All Insider Transaction Types API. This API provides details on various transaction actions, including purchases, sales, and other corporate actions involving insider trading.
* Insider Trade Statistics API: Analyze insider trading activity with the Insider Trade Statistics API. This API provides key statistics on insider transactions, including total purchases, sales, and trends for specific companies or stock symbols.
* Acquisition Ownership API: Track changes in stock ownership during acquisitions using the Acquisition Ownership API. This API provides detailed information on how mergers, takeovers, or beneficial ownership changes impact the stock ownership structure of a company.

## Indexes
* Stock Market Indexes List API: Retrieve a comprehensive list of stock market indexes across global exchanges using the FMP Stock Market Indexes List API. This API provides essential information such as the symbol, name, exchange, and currency for each index, helping analysts and investors keep track of various market benchmarks.
* Index Quote API: Access real-time stock index quotes with the Stock Index Quote API. Stay updated with the latest price changes, daily highs and lows, volume, and other key metrics for major stock indices around the world.
* Index Short Quote API: Access concise stock index quotes with the Stock Index Short Quote API. This API provides a snapshot of the current price, change, and volume for stock indexes, making it ideal for users who need a quick overview of market movements.
* All Index Quotes API: The All Index Quotes API provides real-time quotes for a wide range of stock indexes, from major market benchmarks to niche indexes. This API allows users to track market performance across multiple indexes in a single request, giving them a broad view of the financial markets.
* Historical Index Light Chart API: Retrieve end-of-day historical prices for stock indexes using the Historical Price Data API. This API provides essential data such as date, price, and volume, enabling detailed analysis of price movements over time.
* Historical Index Full Chart API: Access full historical end-of-day prices for stock indexes using the Detailed Historical Price Data API. This API provides comprehensive information, including open, high, low, close prices, volume, and additional metrics for detailed financial analysis.
* 1-Minute Interval Index Price API: Retrieve 1-minute interval intraday data for stock indexes using the Intraday 1-Minute Price Data API. This API provides granular price information, helping users track short-term price movements and trading volume within each minute.
* 5-Minute Interval Index Price API: Retrieve 5-minute interval intraday price data for stock indexes using the Intraday 5-Minute Price Data API. This API provides crucial insights into price movements and trading volume within 5-minute windows, ideal for traders who require short-term data.
* 1-Hour Interval Index Price API: Access 1-hour interval intraday data for stock indexes using the Intraday 1-Hour Price Data API. This API provides detailed price movements and volume within hourly intervals, making it ideal for tracking medium-term market trends during the trading day.
* S&P 500 Index API: Access detailed data on the S&P 500 index using the S&P 500 Index API. Track the performance and key information of the companies that make up this major stock market index.
* Nasdaq Index API: Access comprehensive data for the Nasdaq index with the Nasdaq Index API. Monitor real-time movements and track the historical performance of companies listed on this prominent stock exchange.
* Dow Jones API: Access data on the Dow Jones Industrial Average using the Dow Jones API. Track current values, analyze trends, and get detailed information about the companies that make up this important stock index.
* Historical S&P 500 API: Retrieve historical data for the S&P 500 index using the Historical S&P 500 API. Analyze past changes in the index, including additions and removals of companies, to understand trends and performance over time.
* Historical Nasdaq API: Access historical data for the Nasdaq index using the Historical Nasdaq API. Analyze changes in the index composition and view how it has evolved over time, including company additions and removals.
* Historical Dow Jones API: Access historical data for the Dow Jones Industrial Average using the Historical Dow Jones API. Analyze changes in the index’s composition and study its performance across different periods.

## Market Hours
* Global Exchange Market Hours API: Retrieve trading hours for specific stock exchanges using the Global Exchange Market Hours API. Find out the opening and closing times of global exchanges to plan your trading strategies effectively.
* Holidays By Exchange API: 
* All Exchange Market Hours API: View the market hours for all exchanges. Check when different markets are active.

## Commodity
* Commodities List API: Access an extensive list of tracked commodities across various sectors, including energy, metals, and agricultural products. The FMP Commodities List API provides essential data on tradable commodities, giving investors the ability to explore market options in real-time.
* Commodities Quote API: Access real-time price quotes for all commodities traded worldwide with the FMP Global Commodities Quotes API. Track market movements and identify investment opportunities with comprehensive price data.
* Commodities Quote Short API: Get fast and accurate quotes for commodities with the FMP Commodities Quick Quote API. Instantly access the current price, recent changes, and trading volume for various commodities in real-time.
* All Commodities Quotes API: Access real-time quotes for multiple commodities at once with the FMP Real-Time Batch Commodities Quotes API. Instantly track price changes, volume, and other key metrics for a broad range of commodities.
* Light Chart API: Access historical end-of-day prices for various commodities with the FMP Historical Commodities Price API. Analyze past price movements, trading volume, and trends to support informed decision-making.
* Full Chart API: Access full historical end-of-day price data for commodities with the FMP Comprehensive Commodities Price API. This API enables users to analyze long-term price trends, patterns, and market movements in great detail.
* 1-Minute Interval Commodities Chart API: Track real-time, short-term price movements for commodities with the FMP 1-Minute Interval Commodities Chart API. This API provides detailed 1-minute interval data, enabling precise monitoring of intraday market changes.
* 5-Minute Interval Commodities Chart API: Monitor short-term price movements with the FMP 5-Minute Interval Commodities Chart API. This API provides detailed 5-minute interval data, enabling users to track near-term price trends for more strategic trading and investment decisions.
* 1-Hour Interval Commodities Chart API: Monitor hourly price movements and trends with the FMP 1-Hour Interval Commodities Chart API. This API provides hourly data, offering a detailed look at price fluctuations throughout the trading day to support mid-term trading strategies and market analysis.

## Discounted Cash Flow
* DCF Valuation API: Estimate the intrinsic value of a company with the FMP Discounted Cash Flow Valuation API. Calculate the DCF valuation based on expected future cash flows and discount rates.
* Levered DCF API: Analyze a company’s value with the FMP Levered Discounted Cash Flow (DCF) API, which incorporates the impact of debt. This API provides post-debt company valuation, offering investors a more accurate measure of a company's true worth by accounting for its debt obligations.
* Custom DCF Advanced API: Run a tailored Discounted Cash Flow (DCF) analysis using the FMP Custom DCF Advanced API. With detailed inputs, this API allows users to fine-tune their assumptions and variables, offering a more personalized and precise valuation for a company.
* Custom DCF Levered API: Run a tailored Discounted Cash Flow (DCF) analysis using the FMP Custom DCF Advanced API. With detailed inputs, this API allows users to fine-tune their assumptions and variables, offering a more personalized and precise valuation for a company.

## Forex
* Forex Currency Pairs API: Access a comprehensive list of all currency pairs traded on the forex market with the FMP Forex Currency Pairs API. Analyze and track the performance of currency pairs to make informed investment decisions.
* Forex Quote API: Access real-time forex quotes for currency pairs with the Forex Quote API. Retrieve up-to-date information on exchange rates and price changes to help monitor market movements.
* Forex Short Quote API: Quickly access concise forex pair quotes with the Forex Quote Snapshot API. Get a fast look at live currency exchange rates, price changes, and volume in real time.
* Batch Forex Quotes API: Easily access real-time quotes for multiple forex pairs simultaneously with the Batch Forex Quotes API. Stay updated on global currency exchange rates and monitor price changes across different markets.
* Historical Forex Light Chart API: Access historical end-of-day forex prices with the Historical Forex Light Chart API. Track long-term price trends across different currency pairs to enhance your trading and analysis strategies.
* Historical Forex Full Chart API: Access comprehensive historical end-of-day forex price data with the Full Historical Forex Chart API. Gain detailed insights into currency pair movements, including open, high, low, close (OHLC) prices, volume, and percentage changes.
* 1-Minute Interval Forex Chart API: Access real-time 1-minute intraday forex data with the 1-Minute Forex Interval Chart API. Track short-term price movements for precise, up-to-the-minute insights on currency pair fluctuations.
* 5-Minute Interval Forex Chart API: Track short-term forex trends with the 5-Minute Forex Interval Chart API. Access detailed 5-minute intraday data to monitor currency pair price movements and market conditions in near real-time.
* 1-Hour Interval Forex Chart API: Track forex price movements over the trading day with the 1-Hour Forex Interval Chart API. This tool provides hourly intraday data for currency pairs, giving a detailed view of trends and market shifts.

## Crypto
* Cryptocurrency List API: Access a comprehensive list of all cryptocurrencies traded on exchanges worldwide with the FMP Cryptocurrencies Overview API. Get detailed information on each cryptocurrency to inform your investment strategies.
* Full Cryptocurrency Quote API: Access real-time quotes for all cryptocurrencies with the FMP Full Cryptocurrency Quote API. Obtain comprehensive price data including current, high, low, and open prices.
* Cryptocurrency Quote Short API: Access real-time cryptocurrency quotes with the FMP Cryptocurrency Quick Quote API. Get a concise overview of current crypto prices, changes, and trading volume for a wide range of digital assets.
* All Cryptocurrencies Quotes API: Access live price data for a wide range of cryptocurrencies with the FMP Real-Time Cryptocurrency Batch Quotes API. Get real-time updates on prices, market changes, and trading volumes for digital assets in a single request.
* Historical Cryptocurrency Light Chart API: Access historical end-of-day prices for a variety of cryptocurrencies with the Historical Cryptocurrency Price Snapshot API. Track trends in price and trading volume over time to better understand market behavior.
* Historical Cryptocurrency Full Chart API: Access comprehensive end-of-day (EOD) price data for cryptocurrencies with the Full Historical Cryptocurrency Data API. Analyze long-term price trends, market movements, and trading volumes to inform strategic decisions.
* 1-Minute Interval Cryptocurrency Data API: Get real-time, 1-minute interval price data for cryptocurrencies with the 1-Minute Cryptocurrency Intraday Data API. Monitor short-term price fluctuations and trading volume to stay updated on market movements.
* 5-Minute Interval Cryptocurrency Data API: Analyze short-term price trends with the 5-Minute Interval Cryptocurrency Data API. Access real-time, intraday price data for cryptocurrencies to monitor rapid market movements and optimize trading strategies.
* 1-Hour Interval Cryptocurrency Data API: Access detailed 1-hour intraday price data for cryptocurrencies with the 1-Hour Interval Cryptocurrency Data API. Track hourly price movements to gain insights into market trends and make informed trading decisions throughout the day.

## Senate
* Latest Senate Financial Disclosures API: Access the latest financial disclosures from U.S. Senate members with the FMP Latest Senate Financial Disclosures API. Track recent trades, asset ownership, and transaction details for enhanced transparency in government financial activities.
* Latest House Financial Disclosures API: Access real-time financial disclosures from U.S. House members with the FMP Latest House Financial Disclosures API. Track recent trades, asset ownership, and financial holdings for enhanced visibility into political figures' financial activities.
* Senate Trading Activity API: Monitor the trading activity of US Senators with the FMP Senate Trading Activity API. Access detailed information on trades made by Senators, including trade dates, assets, amounts, and potential conflicts of interest.
* Senate Trades By Name API: 
* U.S. House Trades API: Track the financial trades made by U.S. House members and their families with the FMP U.S. House Trades API. Access real-time information on stock sales, purchases, and other investment activities to gain insight into their financial decisions.
* House Trades By Name API: 

## ESG
* ESG Investment Search API: Align your investments with your values using the FMP ESG Investment Search API. Discover companies and funds based on Environmental, Social, and Governance (ESG) scores, performance, controversies, and business involvement criteria.
* ESG Ratings API: Access comprehensive ESG ratings for companies and funds with the FMP ESG Ratings API. Make informed investment decisions based on environmental, social, and governance (ESG) performance data.
* ESG Benchmark Comparison API: Evaluate the ESG performance of companies and funds with the FMP ESG Benchmark Comparison API. Compare ESG leaders and laggards within industries to make informed and responsible investment decisions.

## Commitment Of Traders
* COT Report API: Access comprehensive Commitment of Traders (COT) reports with the FMP COT Report API. This API provides detailed information about long and short positions across various sectors, helping you assess market sentiment and track positions in commodities, indices, and financial instruments.
* COT Analysis By Dates API: Gain in-depth insights into market sentiment with the FMP COT Report Analysis API. Analyze the Commitment of Traders (COT) reports for a specific date range to evaluate market dynamics, sentiment, and potential reversals across various sectors.
* COT Report List API: Access a comprehensive list of available Commitment of Traders (COT) reports by commodity or futures contract using the FMP COT Report List API. This API provides an overview of different market segments, allowing users to retrieve and explore COT reports for a wide variety of commodities and financial instruments.

## Fundraisers
* Latest Crowdfunding Campaigns API: Discover the most recent crowdfunding campaigns with the FMP Latest Crowdfunding Campaigns API. Stay informed on which companies and projects are actively raising funds, their financial details, and offering terms.
* Crowdfunding Campaign Search API: Search for crowdfunding campaigns by company name, campaign name, or platform with the FMP Crowdfunding Campaign Search API. Access detailed information to track and analyze crowdfunding activities.
* Crowdfunding By CIK API: Access detailed information on all crowdfunding campaigns launched by a specific company with the FMP Crowdfunding By CIK API.
* Equity Offering Updates API: Stay informed about the latest equity offerings with the FMP Equity Offering Updates API. Track new shares being issued by companies and get insights into exempt offerings and amendments.
* Equity Offering Search API: Easily search for equity offerings by company name or stock symbol with the FMP Equity Offering Search API. Access detailed information about recent share issuances to stay informed on company fundraising activities.
* Equity Offering By CIK API: Access detailed information on equity offerings announced by specific companies with the FMP Company Equity Offerings by CIK API. Track offering activity and identify potential investment opportunities.

## Bulk
* Company Profile Bulk API: The FMP Profile Bulk API allows users to retrieve comprehensive company profile data in bulk. Access essential information, such as company details, stock price, market cap, sector, industry, and more for multiple companies in a single request.
* Stock Rating Bulk API: The FMP Rating Bulk API provides users with comprehensive rating data for multiple stocks in a single request. Retrieve key financial ratings and recommendations such as overall ratings, DCF recommendations, and more for multiple companies at once.
* DCF Valuations Bulk API: The FMP DCF Bulk API enables users to quickly retrieve discounted cash flow (DCF) valuations for multiple symbols in one request. Access the implied price movement and percentage differences for all listed companies.
* Financial Scores Bulk API: The FMP Scores Bulk API allows users to quickly retrieve a wide range of key financial scores and metrics for multiple symbols. These scores provide valuable insights into company performance, financial health, and operational efficiency.
* Price Target Summary Bulk API: The Price Target Summary Bulk API provides a comprehensive overview of price targets for all listed symbols over multiple timeframes. With this API, users can quickly retrieve price target data, helping investors and analysts compare current prices to projected targets across different periods.
* ETF Holder Bulk API: The ETF Holder Bulk API allows users to quickly retrieve detailed information about the assets and shares held by Exchange-Traded Funds (ETFs). This API provides insights into the weight each asset carries within the ETF, along with key financial information related to these holdings.
* Upgrades Downgrades Consensus Bulk API: The Upgrades Downgrades Consensus Bulk API provides a comprehensive view of analyst ratings across all symbols. Retrieve bulk data for analyst upgrades, downgrades, and consensus recommendations to gain insights into the market's outlook on individual stocks.
* Key Metrics TTM Bulk API: The Key Metrics TTM Bulk API allows users to retrieve trailing twelve months (TTM) data for all companies available in the database. The API provides critical financial ratios and metrics based on each company’s latest financial report, offering insights into company performance and financial health.
* Ratios TTM Bulk API: The Ratios TTM Bulk API offers an efficient way to retrieve trailing twelve months (TTM) financial ratios for stocks. It provides users with detailed insights into a company’s profitability, liquidity, efficiency, leverage, and valuation ratios, all based on the most recent financial report.
* Stock Peers Bulk API: The Stock Peers Bulk API allows you to quickly retrieve a comprehensive list of peer companies for all stocks in the database. By accessing this data, you can easily compare a stock’s performance with its closest competitors or similar companies within the same industry or sector.
* Earnings Surprises Bulk API: The Earnings Surprises Bulk API allows users to retrieve bulk data on annual earnings surprises, enabling quick analysis of which companies have beaten, missed, or met their earnings estimates. This API provides actual versus estimated earnings per share (EPS) for multiple companies at once, offering valuable insights for investors and analysts.
* Income Statement Bulk API: The Bulk Income Statement API allows users to retrieve detailed income statement data in bulk. This API is designed for large-scale data analysis, providing comprehensive insights into a company's financial performance, including revenue, gross profit, expenses, and net income.
* Income Statement Growth Bulk API: The Bulk Income Statement Growth API provides access to growth data for income statements across multiple companies. Track and analyze growth trends over time for key financial metrics such as revenue, net income, and operating income, enabling a better understanding of corporate performance trends.
* Balance Sheet Statement Bulk API: The Bulk Balance Sheet Statement API provides comprehensive access to balance sheet data across multiple companies. It enables users to analyze financial positions by retrieving key figures such as total assets, liabilities, and equity. Ideal for comparing the financial health and stability of different companies on a large scale.
* Balance Sheet Statement Growth Bulk API: The Balance Sheet Growth Bulk API allows users to retrieve growth data across multiple companies’ balance sheets, enabling detailed analysis of how financial positions have changed over time.
* Cash Flow Statement Bulk API: The Cash Flow Statement Bulk API provides access to detailed cash flow reports for a wide range of companies. This API enables users to retrieve bulk cash flow statement data, helping to analyze companies’ operating, investing, and financing activities over time.
* Cash Flow Statement Growth Bulk API: The Cash Flow Statement Growth Bulk API allows you to retrieve bulk growth data for cash flow statements, enabling you to track changes in cash flows over time. This API is ideal for analyzing the cash flow growth trends of multiple companies simultaneously.
* Eod Bulk API: The EOD Bulk API allows users to retrieve end-of-day stock price data for multiple symbols in bulk. This API is ideal for financial analysts, traders, and investors who need to assess valuations for a large number of companies.

—------

# Alphavantage:

## Time Series Stock Data APIs
* `TIME_SERIES_INTRADAY`: This API returns current and 20+ years of historical intraday OHLCV time series of the equity specified, covering pre-market and post-market hours where applicable (e.g., 4:00am to 8:00pm Eastern Time for the US market). You can query both raw (as-traded) and split/dividend-adjusted intraday data from this endpoint. The OHLCV data is sometimes called "candles" in finance literature. 
* `TIME_SERIES_DAILY`: This API returns raw (as-traded) daily time series (date, daily open, daily high, daily low, daily close, daily volume) of the global equity specified, covering 20+ years of historical data. The OHLCV data is sometimes called "candles" in finance literature. If you are also interested in split/dividend-adjusted data, please use the Daily Adjusted API, which covers adjusted close values and historical split and dividend events.
* `TIME_SERIES_DAILY_ADJUSTED`: This API returns raw (as-traded) daily open/high/low/close/volume values, adjusted close values, and historical split/dividend events of the global equity specified, covering 20+ years of historical data. The OHLCV data is sometimes called "candles" in finance literature.
* `TIME_SERIES_WEEKLY`: This API returns weekly time series (last trading day of each week, weekly open, weekly high, weekly low, weekly close, weekly volume) of the global equity specified, covering 20+ years of historical data.
* `TIME_SERIES_WEEKLY_ADJUSTED`: This API returns weekly adjusted time series (last trading day of each week, weekly open, weekly high, weekly low, weekly close, weekly adjusted close, weekly volume, weekly dividend) of the global equity specified, covering 20+ years of historical data.
* `TIME_SERIES_MONTHLY`: This API returns monthly time series (last trading day of each month, monthly open, monthly high, monthly low, monthly close, monthly volume) of the global equity specified, covering 20+ years of historical data.
* `TIME_SERIES_MONTHLY_ADJUSTED`: This API returns monthly adjusted time series (last trading day of each month, monthly open, monthly high, monthly low, monthly close, monthly adjusted close, monthly volume, monthly dividend) of the equity specified, covering 20+ years of historical data.
* `Quote Endpoint`: This endpoint returns the latest price and volume information for a ticker of your choice. You can specify one ticker per API request.
* `Realtime Bulk Quotes`: This API returns realtime quotes for US-traded symbols in bulk, accepting up to 100 symbols per API request and covering both regular and extended (pre-market and post-market) trading hours. You can use this endpoint as a high-throughput alternative to the Global Quote API, which accepts one symbol per API request.
* `Search Endpoint`: Looking for some specific symbols or companies? Trying to build an auto-complete search box similar to the one below? We've got you covered! The Search Endpoint returns the best-matching symbols and market information based on keywords of your choice. The search results also contain match scores that provide you with the full flexibility to develop your own search and filtering logic.
* `Global Market Open & Close Status`: This endpoint returns the current market status (open vs. closed) of major trading venues for equities, forex, and cryptocurrencies around the world.

## Options Data APIs
* `Realtime Options`: This API returns realtime US options data with full market coverage. Option chains are sorted by expiration dates in chronological order. Within the same expiration date, contracts are sorted by strike prices from low to high. 
* `Historical Options`: This API returns the full historical options chain for a specific symbol on a specific date, covering 15+ years of history. Implied volatility (IV) and common Greeks (e.g., delta, gamma, theta, vega, rho) are also returned. Option chains are sorted by expiration dates in chronological order. Within the same expiration date, contracts are sorted by strike prices from low to high.

## Alpha Intelligence™
* `Market News & Sentiment`: Looking for market news data to train your LLM models or to augment your trading strategy? You have just found it. This API returns live and historical market news & sentiment data from a large & growing selection of premier news outlets around the world, covering stocks, cryptocurrencies, forex, and a wide range of topics such as fiscal policy, mergers & acquisitions, IPOs, etc. This API, combined with our core stock API, fundamental data, and technical indicator APIs, can provide you with a 360-degree view of the financial market and the broader economy.
* `Earnings Call Transcript`: This API returns the earnings call transcript for a given company in a specific quarter, covering over 15 years of history and enriched with LLM-based sentiment signals.
* `Top Gainers, Losers, and Most Actively Traded Tickers (US Market)`: This endpoint returns the top 20 gainers, losers, and the most active traded tickers in the US market.
* `Insider Transactions`: This API returns the latest and historical insider transactions made by key stakeholders (e.g., founders, executives, board members, etc.) of a specific company.
* `Advanced Analytics (Fixed Window)`: This endpoint returns a rich set of advanced analytics metrics (e.g., total return, variance, auto-correlation, etc.) for a given time series over a fixed temporal window.
* `Advanced Analytics (Sliding Window)`: This endpoint returns a rich set of advanced analytics metrics (e.g., total return, variance, auto-correlation, etc.) for a given time series over sliding time windows. For example, we can calculate a moving variance over 5 years with a window of 100 points to see how the variance changes over time. 

## Fundamental Data
* `Company Overview`: This API returns the company information, financial ratios, and other key metrics for the equity specified. Data is generally refreshed on the same day a company reports its latest earnings and financials.
* `ETF Profile & Holdings`: This API returns key ETF metrics (e.g., net assets, expense ratio, and turnover), along with the corresponding ETF holdings / constituents with allocation by asset types and sectors.
* `Corporate Action - Dividends`: This API returns historical and future (declared) dividend distributions.
* `Corporate Action - Splits`: This API returns historical split events.
* `INCOME_STATEMENT`: This API returns the annual and quarterly income statements for the company of interest, with normalized fields mapped to GAAP and IFRS taxonomies of the SEC. Data is generally refreshed on the same day a company reports its latest earnings and financials.
* `BALANCE_SHEET`: This API returns the annual and quarterly balance sheets for the company of interest, with normalized fields mapped to GAAP and IFRS taxonomies of the SEC. Data is generally refreshed on the same day a company reports its latest earnings and financials.
* `CASH_FLOW`: This API returns the annual and quarterly cash flow for the company of interest, with normalized fields mapped to GAAP and IFRS taxonomies of the SEC. Data is generally refreshed on the same day a company reports its latest earnings and financials.
* `SHARES_OUTSTANDING`: This API returns the quarterly numbers of shares outstanding for the company of interest, with both diluted and basic shares outstanding values returned. Data is generally refreshed on the same day a company reports its latest earnings and financials.
* `Earnings History`: This API returns the annual and quarterly earnings (EPS) for the company of interest. Quarterly data also includes analyst estimates and surprise metrics.
* `Earnings Estimates`: This API returns the annual and quarterly EPS and revenue estimates for the company of interest, along with analyst count and revision history.
* `Listing & Delisting Status`: This API returns a list of active or delisted US stocks and ETFs, either as of the latest trading day or at a specific time in history. The endpoint is positioned to facilitate equity research on asset lifecycle and survivorship.
* `Earnings Calendar`: This API returns a list of company earnings expected in the next 3, 6, or 12 months.
* `IPO Calendar`: This API returns a list of IPOs expected in the next 3 months.

## Foreign Exchange Rates (FX)
* `CURRENCY_EXCHANGE_RATE`: This API returns the realtime exchange rate for a pair of fiat currencies (e.g., USD, EUR, CNY, etc.).
* `FX_INTRADAY`: This API returns intraday time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.
* `FX_DAILY`: This API returns the daily time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime.
* `FX_WEEKLY`: This API returns the weekly time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime. The latest data point is the price information for the week (or partial week) containing the current trading day, updated realtime.
* `FX_MONTHLY`: This API returns the monthly time series (timestamp, open, high, low, close) of the FX currency pair specified, updated realtime. The latest data point is the prices information for the month (or partial month) containing the current trading day, updated realtime.

## Digital & Crypto Currencies
* `CURRENCY_EXCHANGE_RATE`: This API returns the realtime exchange rate for any pair of cryptocurrency (e.g., Bitcoin) or physical currency (e.g., USD).
* `CRYPTO_INTRADAY`: This API returns intraday time series (timestamp, open, high, low, close, volume) of the cryptocurrency specified, updated realtime.
* `DIGITAL_CURRENCY_DAILY`: This API returns the daily historical time series for a cryptocurrency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.
* `DIGITAL_CURRENCY_WEEKLY`: This API returns the weekly historical time series for a cryptocurrency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.
* `DIGITAL_CURRENCY_MONTHLY`: This API returns the monthly historical time series for a cryptocurrency (e.g., BTC) traded on a specific market (e.g., EUR/Euro), refreshed daily at midnight (UTC). Prices and volumes are quoted in both the market-specific currency and USD.

## Commodities
* `Gold & Silver Spot Prices`: This API returns the live spot prices of gold and silver metals.
* `Gold & Silver Historical Prices`: This API returns the historical gold and silver prices in daily, weekly, and monthly horizons.
* `Crude Oil Prices: West Texas Intermediate (WTI)`: This API returns the West Texas Intermediate (WTI) crude oil prices in daily, weekly, and monthly horizons.
* `Crude Oil Prices (Brent)`: This API returns the Brent (Europe) crude oil prices in daily, weekly, and monthly horizons.
* `Natural Gas`: This API returns the Henry Hub natural gas spot prices in daily, weekly, and monthly horizons.
* `Global Price of Copper`: This API returns the global price of copper in monthly, quarterly, and annual horizons.
* `Global Price of Aluminum`: This API returns the global price of aluminum in monthly, quarterly, and annual horizons.
* `Global Price of Wheat`: This API returns the global price of wheat in monthly, quarterly, and annual horizons.
* `Global Price of Corn`: This API returns the global price of corn in monthly, quarterly, and annual horizons.
* `Global Price of Cotton`: This API returns the global price of cotton in monthly, quarterly, and annual horizons.
* `Global Price of Sugar`: This API returns the global price of sugar in monthly, quarterly, and annual horizons.
* `Global Price of Coffee`: This API returns the global price of coffee in monthly, quarterly, and annual horizons.
* `Global Price Index of All Commodities`: This API returns the global price index of all commodities in monthly, quarterly, and annual temporal dimensions.

## Economic Indicators
* `REAL_GDP`: This API returns the annual and quarterly Real GDP of the United States.
* `REAL_GDP_PER_CAPITA`: This API returns the quarterly Real GDP per Capita data of the United States.
* `TREASURY_YIELD`: This API returns the daily, weekly, and monthly US treasury yield of a given maturity timeline (e.g., 5 year, 30 year, etc).
* `FEDERAL_FUNDS_RATE`: This API returns the daily, weekly, and monthly federal funds rate (interest rate) of the United States.
* `CPI`: This API returns the monthly and semiannual consumer price index (CPI) of the United States. CPI is widely regarded as the barometer of inflation levels in the broader economy.
* `INFLATION`: This API returns the annual inflation rates (consumer prices) of the United States.
* `RETAIL_SALES`: This API returns the monthly Advance Retail Sales: Retail Trade data of the United States.
* `DURABLES`: This API returns the monthly manufacturers' new orders of durable goods in the United States.
* `UNEMPLOYMENT`: This API returns the monthly unemployment data of the United States. The unemployment rate represents the number of unemployed as a percentage of the labor force.
* `NONFARM_PAYROLL`: This API returns the monthly US All Employees: Total Nonfarm (commonly known as Total Nonfarm Payroll), a measure of the number of U.S. workers in the economy that excludes proprietors, private household employees, unpaid volunteers, farm employees, and the unincorporated self-employed.

## Technical Indicators
* `SMA` Trending
* `EMA` Trending
* `WMA`
* `DEMA`
* `TEMA`
* `TRIMA`
* `KAMA`
* `MAMA`
* `VWAP` Premium
* `T3`
* `MACD` Premium
* `MACDEXT`
* `STOCH` Trending
* `STOCHF`
* `RSI` Trending
* `STOCHRSI`
* `WILLR`
* `ADX` Trending
* `ADXR`
* `APO`
* `PPO`
* `MOM`
* `BOP`
* `CCI` Trending
* `CMO`
* `ROC`
* `ROCR`
* `AROON` Trending
* `AROONOSC`
* `MFI`
* `TRIX`
* `ULTOSC`
* `DX`
* `MINUS_DI`
* `PLUS_DI`
* `MINUS_DM`
* `PLUS_DM`
* `BBANDS` Trending
* `MIDPOINT`
* `MIDPRICE`
* `SAR`
* `TRANGE`
* `ATR`
* `NATR`
* `AD` Trending
* `ADOSC`
* `OBV` Trending
* `HT_TRENDLINE`
* `HT_SINE`
* `HT_TRENDMODE`
* `HT_DCPERIOD`
* `HT_DCPHASE`
* `HT_PHASOR`

# Sociavault:
## TikTok
* `GET Profile`
* `GET User's Audience Demographics`
* `GET Profile Videos`
* `GET Video Info`
* `GET Transcript`
* `GET TikTok Live`
* `GET Comments`
* `GET Following`
* `GET Followers`
* `GET Search Users`
* `GET Search by Hashtag`
* `GET Search by Keyword`
* `GET Search Music`
* `GET Top Search`
* `GET Get popular songs`
* `GET Get Popular Creators`
* `GET Get Popular Videos`
* `GET Get Popular Hashtags`
* `GET Get Song Details`
* `GET TikToks using Song`
* `GET Trending Feed`

## TikTok Shop
* `GET Shop Products`
* `GET Product Details`
* `GET Shop Search`
* `GET Product Reviews`

## Instagram
* `GET Profile`
* `GET Posts`
* `GET Post/Reel Info`
* `GET Transcript`
* `GET Comments`
* `GET Reels`
* `GET Story Highlights`
* `GET Highlights Details`
* `GET Reels using Song`

## YouTube
* `GET Channel Details`
* `GET Channel Videos`
* `GET Channel Shorts`
* `GET Video/Short Details`
* `GET Transcript`
* `GET Search`
* `GET Search by Hashtag`
* `GET Comments`
* `GET Trending Shorts`

## LinkedIn
* `GET Person's Profile`
* `GET Company Page`
* `GET Post`

## Facebook
* `GET Profile`
* `GET Profile Posts`
* `GET Profile Reels`
* `GET Facebook Group Posts`
* `GET Post`
* `GET Transcript`
* `GET Comments`

## Facebook Ad Library
* `GET Ad Details`
* `GET Search`
* `GET Company Ads`
* `GET Search for Companies`

## Google Ad Library
* `GET Company Ads`
* `GET Ad Details`
* `GET Search Advertisers`

## LinkedIn Ad Library
* `GET Search Ads`
* `GET Ad Details`

## Twitter
* `GET Profile`
* `GET User Tweets`
* `GET Tweet Details`
* `GET Transcript`
* `GET Community`
* `GET Community Tweets`

## Reddit
* `GET Subreddit Details`
* `GET Subreddit Posts`
* `GET Subreddit Search`
* `GET Post Comments`
* `GET Search`
* `GET Search Ads`
* `GET Get Ad`

## Threads
* `GET Profile`
* `GET Posts`
* `GET Post`
* `GET Search Users`

## Google
* `GET Search`

## Pinterest
* `GET Search`
* `GET Pin`
* `GET User Boards`
* `GET Board`

## Account
* `GET Get Credits Balance`

# Perigon:

## Search & Filtering
* `Query Logic & Keywords`: Harnesses the firehose of news using Boolean logic, exact phrases, and wildcards to pinpoint exact topics and filter out noise.
* `Highlights`: Enables HTML-style highlighting in search results to help you quickly spot the most relevant snippets within article fields. 
* `Dates & Times`: Filters content using ISO 8601 formatted temporal ranges for precise day, hour, or minute-level slicing.
* `Location & Geo Coordinates`: Targets content based on mentioned places or publisher locations using cities, states, countries, or geographic coordinate radiuses. 
* `Entities`: Steers search results by including or excluding specific people, companies, or journalists using exact names or unique identifiers.
* `Topics & Types`: Categorizes and filters content across five axes—categories, topics, taxonomies, medium, and editorial labels.
* `Sources & Source Groups`: Targets or excludes specific publisher domains or leverages Perigon's pre-curated bundles of top media outlets.
* `Deduplication & Reprints`: Cleans up your feed by flagging and allowing you to hide syndicated reprints and duplicate story clusters.
* `Languages`: Filters the news feed to return content written in specifically targeted languages.
* `Pagination`: Manages large result sets by retrieving data in smaller, zero-indexed pages of up to 100 items per request.
* `Sentiment`: Analyzes and filters content based on its emotional tone, scoring it across positive, negative, and neutral dimensions.

## Advanced Search & AI
* `Summarizer`: Combines factual extraction with LLM-powered language to generate a short, readable summary based on your article or cluster query. 
* `Vector Search`: Uses an open-weight transformer to embed natural language prompts and find semantically similar articles without complex Boolean logic. 
* `MCP`: Provides a Model Context Protocol server that allows AI assistants to securely connect to Perigon's real-time news data and specialized endpoints.
* `MCP Use Cases`: Offers built-in tools for AI assistants to natively execute advanced searches across articles, stories, journalists, sources, people, companies, and Wikipedia data.

## Additional Content
* `Image Payloads`: Returns URLs for large full logos, square brand markers, and favicons belonging to major media sources.
* `Local News`: Optimizes searches to deliver comprehensive local news coverage from broadcasters and publishers in specific structured metropolitan areas.

## Utilities
* `Utilities`: Provides supplementary data endpoints and helper functions for interacting seamlessly with the broader Perigon platform.