---
layout: project_page
permalink: /

title: "SVBench: A Benchmark with Temporal Multi-Turn Dialogues for Streaming Video Understanding"
authors:
    Zhenyu Yang<sup><span style="color:blue">1</span>,<span style="color:green">2</span>,<span style="color:orange">3</span></sup>, Yuhang Hu<sup><span style="color:purple">4</span></sup>, Zemin Du<sup><span style="color:brown">5</span></sup>, Dizhan Xue<sup><span style="color:blue">1</span>,<span style="color:green">2</span></sup>, Shengsheng Qian<sup><span style="color:blue">1</span>,<span style="color:green">2</span></sup>, Jiahong Wu<sup><span style="color:orange">3</span></sup>, Fan Yang<sup><span style="color:orange">3</span></sup>, Weiming Dong<sup><span style="color:blue">1</span>,<span style="color:green">2</span></sup>, Changsheng Xu<sup><span style="color:blue">1</span>,<span style="color:green">2</span>,<span style="color:red">6</span></sup>
affiliations:
    <sup><span style="color:blue">1</span></sup>Institute of Automation, Chinese Academy of Sciences, <sup><span style="color:green">2</span></sup>University of Chinese Academy of Sciences, <sup><span style="color:orange">3</span></sup>Kuaishou Technology, <sup><span style="color:purple">4</span></sup>Zhengzhou University, <sup><span style="color:brown">5</span></sup>ShanghaiTech University, <sup><span style="color:red">6</span></sup>Peng Cheng Laboratory
conference:
    <strong><span style="color:gray">ICLR'2025</span> (<span style="color:red">Spotlight</span>🔥)</strong>
paper: https://openreview.net/pdf?id=Hz4BYVY8YM
video: https://www.youtube.com/results?search_query=turing+machine
code: https://github.com/yzy-bupt/SVBench
data: https://huggingface.co/docs/datasets
---

<!-- Using HTML to center the abstract -->
<div class="columns is-centered has-text-centered">
    <div class="column is-four-fifths">
        <h2>Abstract</h2>
        <div class="content has-text-justified">
Despite the significant advancements of Large Vision-Language Models (LVLMs) on established benchmarks, there remains a notable gap in suitable evaluation regarding their applicability in the emerging domain of long-context streaming video understanding. Current benchmarks for video understanding typically emphasize isolated single-instance text inputs and fail to evaluate the capacity to sustain temporal reasoning throughout the entire duration of video streams. To address these limitations, we introduce SVBench, a pioneering benchmark with temporal multi-turn question-answering chains specifically designed to thoroughly assess the capabilities of streaming video understanding of current LVLMs. We design a semi-automated annotation pipeline to obtain 49,979 Question-Answer (QA) pairs of 1,353 streaming videos, which includes generating QA chains that represent a series of consecutive multi-turn dialogues over video segments and constructing temporal linkages between successive QA chains. Our experimental results, obtained from 14 models in dialogue and streaming evaluations, reveal that while the closed-source GPT-4o outperforms others, most open-source LVLMs struggle with long-context streaming video understanding. We also construct a StreamingChat model, which significantly outperforms open-source LVLMs on our SVBench and achieves comparable performance on diverse vision-language benchmarks. We expect SVBench to advance the research of streaming video understanding by providing a comprehensive and in-depth analysis of current LVLMs. Our benchmark and model can be accessed at <a href="https://github.com/yzy-bupt/SVBench">https://github.com/yzy-bupt/SVBench</a>.
        </div>
    </div>
</div>

---

## **Demo**
<video autoplay controls muted loop playsinline height="100%">
  <source src="/static/video/demo_mini.mp4" type="video/mp4">
</video>
> This is a data demo in our SVBench. The video is playing at 2x speed.

## **Overview**
A **temporal dialogue path** represents a conversation within a video progressing over time. Our **SVBench** evaluates the capabilities of LVLMs in **long-context streaming video understanding** by constructing **temporal dialogue paths** to assess **9** critical skills.

![overview](/static/image/overview.png)

*Figure 1: Illustration of temporal multi-turn dialogues.*

## **Annotation Pipeline**
> Overview of the proposed **SVBench** framework: \\
(1) Filtering raw videos from diverse streaming sources; 
(2) Detecting scenes and splitting videos accordingly; 
(3) Constructing QA chains for dialogues within videos; 
(4) Performing manual annotation and quality assessment; 
(5) Identifying temporal linkages between QA chains; 
(6) Connecting QA chains to facilitate temporal reasoning; 
(7) Building temporal dialogue paths for evaluating LVLMs.

![framework](/static/image/framework.png)

*Figure 2: Overview of the proposed SVBench framework.*

## **Statistical Analysis**
Our dataset contains videos organized into **12** primary categories and **36** subcategories. To facilitate a more comprehensive evaluation of the capabilities of LVLMs, we classify the questions into **9** distinct categories.

![ring](/static/image/ring.png)

*Figure 3: Distributions of videos and QA categories.*

## **Leaderboard**
To evaluate the performance of current LVLMs in **streaming video understanding**, we design two distinct experimental setups within the SVBench evaluation set to rigorously assess the capabilities of these LVLMs. 


<table>
  <thead>
    <tr style="background-color: #f2f2f2;">
      <th rowspan="2" style="text-align: center;">Model</th>
      <th colspan="6" style="text-align: center;">Dialogue Evaluation</th>
      <th colspan="6" style="text-align: center;">Streaming Evaluation</th>
    </tr>
    <tr style="background-color: #f2f2f2;">
      <th>SA</th>
      <th>CC</th>
      <th>LC</th>
      <th>TU</th>
      <th>IC</th>
      <th>OS</th>
      <th>SA</th>
      <th>CC</th>
      <th>LC</th>
      <th>TU</th>
      <th>IC</th>
      <th>OS</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #e6e6e6;">
      <td colspan="13" style="text-align: center;"><strong>Open-source LVLMs</strong></td>
    </tr>
    <tr>
      <td>MovieChat</td>
      <td>20.46</td>
      <td>20.05</td>
      <td>27.76</td>
      <td>21.81</td>
      <td>22.21</td>
      <td>21.89</td>
      <td>17.99</td>
      <td>16.42</td>
      <td>20.37</td>
      <td>15.77</td>
      <td>19.08</td>
      <td>17.43</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td>Video-ChatGPT</td>
      <td>31.86</td>
      <td>32.58</td>
      <td>40.28</td>
      <td>35.32</td>
      <td>36.26</td>
      <td>33.80</td>
      <td>27.98</td>
      <td>29.54</td>
      <td>33.81</td>
      <td>27.95</td>
      <td>31.00</td>
      <td>28.88</td>
    </tr>
    <tr>
      <td>Video-LLaVA</td>
      <td>35.62</td>
      <td>36.52</td>
      <td>42.93</td>
      <td>38.63</td>
      <td>38.84</td>
      <td>37.34</td>
      <td>32.22</td>
      <td>32.83</td>
      <td>36.35</td>
      <td>32.46</td>
      <td>34.54</td>
      <td>32.79</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td>ShareGPT4Video</td>
      <td>39.01</td>
      <td>40.42</td>
      <td>47.89</td>
      <td>41.42</td>
      <td>43.18</td>
      <td>40.70</td>
      <td>34.65</td>
      <td>36.70</td>
      <td>41.07</td>
      <td>35.76</td>
      <td>37.22</td>
      <td>35.79</td>
    </tr>
    <tr>
      <td>VideoLLaMA2</td>
      <td>39.13</td>
      <td>40.33</td>
      <td>47.60</td>
      <td>42.36</td>
      <td>41.80</td>
      <td>40.60</td>
      <td>35.68</td>
      <td>36.40</td>
      <td>42.23</td>
      <td>34.65</td>
      <td>36.70</td>
      <td>35.84</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td>TimeChat</td>
      <td>36.19</td>
      <td>37.06</td>
      <td>44.72</td>
      <td>40.42</td>
      <td>37.12</td>
      <td>37.22</td>
      <td>35.72</td>
      <td>37.88</td>
      <td>42.65</td>
      <td>36.23</td>
      <td>36.34</td>
      <td>36.32</td>
    </tr>
    <tr>
      <td>InternVL2</td>
      <td>45.91</td>
      <td>46.30</td>
      <td>52.67</td>
      <td>49.81</td>
      <td>46.25</td>
      <td>46.13</td>
      <td>43.55</td>
      <td>44.10</td>
      <td>48.91</td>
      <td>40.95</td>
      <td>44.17</td>
      <td>42.71</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td>VILA</td>
      <td>46.83</td>
      <td>48.41</td>
      <td>54.92</td>
      <td>48.30</td>
      <td>50.12</td>
      <td>48.51</td>
      <td>46.19</td>
      <td>47.95</td>
      <td>51.60</td>
      <td>44.84</td>
      <td>48.56</td>
      <td>46.26</td>
    </tr>
    <tr>
      <td>InternLM-XC2.5</td>
      <td>51.57</td>
      <td>53.93</td>
      <td>59.69</td>
      <td>51.57</td>
      <td><u>56.28</u></td>
      <td>52.31</td>
      <td>52.22</td>
      <td>53.39</td>
      <td>58.14</td>
      <td>48.05</td>
      <td><u>54.79</u></td>
      <td>51.46</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td>MiniCPM-V 2.6</td>
      <td><u>53.50</u></td>
      <td><u>55.42</u></td>
      <td><u>60.88</u></td>
      <td><u>55.03</u></td>
      <td>55.78</td>
      <td><u>54.30</u></td>
      <td><u>53.33</u></td>
      <td><u>54.30</u></td>
      <td><u>58.97</u></td>
      <td><u>49.64</u></td>
      <td>54.71</td>
      <td><u>52.19</u></td>
    </tr>
    <tr>
      <td>StreamingChat</td>
      <td><strong>59.48</strong></td>
      <td><strong>61.31</strong></td>
      <td><strong>66.05</strong></td>
      <td><strong>58.61</strong></td>
      <td><strong>61.09</strong></td>
      <td><strong>59.41</strong></td>
      <td><strong>55.10</strong></td>
      <td><strong>56.66</strong></td>
      <td><strong>60.72</strong></td>
      <td><strong>51.78</strong></td>
      <td><strong>55.87</strong></td>
      <td><strong>53.90</strong></td>
    </tr>
    <tr style="background-color: #e6e6e6;">
      <td colspan="13" style="text-align: center;"><strong>Closed-source LVLMs</strong></td>
    </tr>
    <tr>
      <td>Gemini 1.5 Pro</td>
      <td>54.89</td>
      <td>56.05</td>
      <td>61.45</td>
      <td>53.08</td>
      <td>56.06</td>
      <td>54.29</td>
      <td>49.06</td>
      <td>50.05</td>
      <td>54.62</td>
      <td>45.73</td>
      <td>49.84</td>
      <td>48.02</td>
    </tr>
    <tr style="background-color: #f9f9f9;">
      <td>GPT-4V</td>
      <td>65.56</td>
      <td>68.02</td>
      <td>71.78</td>
      <td>63.80</td>
      <td>68.01</td>
      <td>65.19</td>
      <td>58.82</td>
      <td>59.55</td>
      <td>64.29</td>
      <td>54.08</td>
      <td>60.61</td>
      <td>57.35</td>
    </tr>
    <tr>
      <td>GPT-4o</td>
      <td><strong>65.73</strong></td>
      <td><strong>68.10</strong></td>
      <td><strong>71.95</strong></td>
      <td><strong>66.54</strong></td>
      <td><strong>68.40</strong></td>
      <td><strong>66.29</strong></td>
      <td><strong>59.52</strong></td>
      <td><strong>60.42</strong></td>
      <td><strong>65.45</strong></td>
      <td><strong>55.10</strong></td>
      <td><strong>61.36</strong></td>
      <td><strong>58.17</strong></td>
    </tr>
  </tbody>
</table>
*Table 1: Evaluation results of various models on SVBench in dialogue and streaming evaluation.*

## **Comparisons with Existing Benchmarks**

**Avg. Q/V**: the average number of QA pairs per video. **Open-Domain**: whether the video sources are diverse. **Long**: whether the average video length is greater than 2 minutes. **Dialogue**: whether there are contextual connections between QA pairs. **Streaming**: whether the QA pairs can be tested in sync with the video over time.

![comparison](/static/image/comp.png)

*Table 2: The comparison of different datasets.*

## **StreamingChat**

Built upon InternVL2, we develop a streaming LVLM baseline named **StreamingChat**. It comprises a vision encoder (InternViT), an MLP projector, and an LLM (InternLM2).

![model_framework](/static/image/model_framework.png)

*Figure 4: Architecture of the proposed StreamingChat model.*



## Citation
```
@article{yang2025svbench,
  title={SVBench: A Benchmark with Temporal Multi-Turn Dialogues for Streaming Video Understanding},
  author={Yang, Zhenyu and Hu, Yuhang and Du, Zemin and Xue, Dizhan and Qian, Shengsheng and Wu, Jiahong and Yang, Fan and Dong, Weiming and Xu, Changsheng},
  journal={arXiv preprint arXiv:2502.10810},
  year={2025}
}
```
