---
# Leave the homepage title empty to use the site title
title:
date: 2022-10-24
type: landing

sections:
  - block: lab-profile
    id: about
    content:
        title: Biography
        # Choose a user profile to display (a folder name within `content/authors/`)
        username: lab
  
  - block: collection
    content:
      archive:
        enable: true
        text: 查看所有资讯
        link: post/
      title: 最新资讯
      subtitle: 
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
      sort_by: 'date'
    design:
      view: compact
      columns: '1'


  - block: markdown
    content:
      title: 研究方向
      subtitle:
      text: |
        （这里对研究方向进行一个总体的概括...）目前的研究方向包括：</br>
        * [**检索增强生成**](publication/#rag)1：子方向1，子方向2，子方向3
        * **大方向**2：子方向1，子方向2，子方向3
        * **大方向**3：子方向1，子方向2，子方向3  
    design:
      columns: '1'

  # - block: tag_cloud
  #   content:
  #     title: My title
  #     subtitle: My subtitle
  #     text: Add any **markdown** formatted content here - text, images, videos, galleries - and even HTML code!
  #     # Choose a taxonomy from the `taxonomies` list in `config.yaml` to display (e.g. tags, categories, authors)
  #     taxonomy: tags
  #     # Choose how many tags you would like to display (0 = all tags)
  #     count: 20
  #   design:
  #     # Minimum and maximum font sizes (1.0 = 100%).
  #     font_size_min: 0.7
  #     font_size_max: 2.0

  - block: collection
    id: pub
    content:
      archive:
        enable: true
        text: 查看所有论文
        link: publication/
      title: 论文发表
      subtitle: 
      text:
      count: 5
      filters:
        folders:
          - publication
      offset: 0
      sort_by: 'Date'
    design:
      view: citation
      columns: '1'


  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="查看我们的团队 →" %}}
    design:
      columns: '1'



---
