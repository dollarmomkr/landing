const Parser = require('rss-parser');
const parser = new Parser({
  headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36' }
});

module.exports = async (req, res) => {
  try {
    // 구글 뉴스 RSS (검색어: 달러)
    const rssUrl = 'https://news.google.com/rss/search?q=%EB%8B%AC%EB%9F%AC&hl=ko&gl=KR&ceid=KR:ko';
    
    console.log('Fetching News from:', rssUrl);
    
    let feed = await parser.parseURL(rssUrl);
    
    if (!feed || !feed.items) {
        throw new Error('뉴스 피드가 비어있습니다.');
    }

    const items = feed.items.slice(0, 5).map(item => {
      const titleParts = item.title ? item.title.split(' - ') : [];
      let source = 'Google News';
      let title = item.title || '제목 없음';
      
      if (titleParts.length > 1) {
        source = titleParts.pop();
        title = titleParts.join(' - ');
      }

      return {
        title: title,
        link: item.link,
        pubDate: item.pubDate,
        source: source
      };
    });

    res.setHeader('Cache-Control', 's-maxage=3600, stale-while-revalidate');
    res.status(200).json({
      success: true,
      items: items
    });
  } catch (error) {
    console.error('RSS Parsing Error Detail:', error);
    res.status(500).json({
      success: false,
      message: '뉴스를 파싱하는 중 오류가 발생했습니다.',
      error: error.message
    });
  }
};
