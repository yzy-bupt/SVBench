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
paper: https://arxiv.org/abs/2502.10810
code: https://github.com/yzy-bupt/SVBench
data: https://huggingface.co/datasets/yzy666/SVBench
video: https://forms.gle/tmY8PmM5KWSvTGcn7
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


<div style="overflow-x:auto;">
  <table>
    <thead>
      <tr style="background-color: #f2f2f2;">
        <th rowspan="2" style="text-align: center;">Model</th>
        <th rowspan="2" style="text-align: center;">Type</th>
        <th rowspan="2" style="text-align: center;">Size</th>
        <th rowspan="2" style="text-align: center;">F/FPS</th>
        <th colspan="6" style="text-align: center;">Dialogue Evaluation</th>
        <th colspan="6" style="text-align: center;">Streaming Evaluation</th>
        <th rowspan="2" style="text-align: center;">AVG</th>
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
        <td colspan="17" style="text-align: center;"><strong>Open-source LVLMs</strong></td>
      </tr>
      <tr>
        <td style="text-align: center;">MovieChat</td>
        <td style="text-align: center;">VideoLLM</td>
        <td style="text-align: center;">7B</td>
        <td style="text-align: center;">2048</td>
        <td>20.36</td>
        <td>23.74</td>
        <td>28.97</td>
        <td>22.80</td>
        <td>20.51</td>
        <td>22.72</td>
        <td>18.92</td>
        <td>22.38</td>
        <td>26.77</td>
        <td>20.46</td>
        <td>20.98</td>
        <td>19.64</td>
        <td style="text-align: center;">21.18</td>
      </tr>
      <tr style="background-color: #f9f9f9;">
        <td style="text-align: center;">Video-ChatGPT</td>
        <td style="text-align: center;">VideoLLM</td>
        <td style="text-align: center;">7B</td>
        <td style="text-align: center;">100</td>
        <td>28.01</td>
        <td>34.04</td>
        <td>40.89</td>
        <td>35.66</td>
        <td>29.59</td>
        <td>32.24</td>
        <td>22.84</td>
        <td>28.44</td>
        <td>33.93</td>
        <td>26.31</td>
        <td>26.43</td>
        <td>25.02</td>
        <td style="text-align: center;">28.63</td>
      </tr>
      <tr>
        <td style="text-align: center;">Video-LLaVA</td>
        <td style="text-align: center;">VideoLLM</td>
        <td style="text-align: center;">7B</td>
        <td style="text-align: center;">8</td>
        <td>31.85</td>
        <td>38.38</td>
        <td>44.93</td>
        <td>41.54</td>
        <td>32.80</td>
        <td>36.49</td>
        <td>26.95</td>
        <td>33.68</td>
        <td>39.00</td>
        <td>31.83</td>
        <td>31.53</td>
        <td>29.89</td>
        <td style="text-align: center;">33.19</td>
      </tr>
      <tr style="background-color: #f9f9f9;">
        <td style="text-align: center;">TimeChat</td>
        <td style="text-align: center;">VideoLLM</td>
        <td style="text-align: center;">7B</td>
        <td style="text-align: center;">16</td>
        <td>31.09</td>
        <td>38.57</td>
        <td>45.52</td>
        <td>43.37</td>
        <td>31.10</td>
        <td>36.24</td>
        <td>27.14</td>
        <td>34.42</td>
        <td>39.78</td>
        <td>36.80</td>
        <td>31.71</td>
        <td>31.15</td>
        <td style="text-align: center;">33.70</td>
      </tr>
      <tr>
        <td style="text-align: center;">LLaVA-NeXT</td>
        <td style="text-align: center;">VideoLLM</td>
        <td style="text-align: center;">7B</td>
        <td style="text-align: center;">16</td>
        <td>37.71</td>
        <td>44.59</td>
        <td>52.05</td>
        <td>41.80</td>
        <td>36.58</td>
        <td>41.40</td>
        <td>34.29</td>
        <td>39.68</td>
        <td>47.65</td>
        <td>35.33</td>
        <td>36.68</td>
        <td>36.12</td>
        <td style="text-align: center;">38.76</td>
      </tr>
      <tr style="background-color: #f9f9f9;">
        <td style="text-align: center;">ShareGPT4Video</td>
        <td style="text-align: center;">VideoLLM</td>
        <td style="text-align: center;">8B</td>
        <td style="text-align: center;">16</td>
        <td>36.26</td>
        <td>43.68</td>
        <td>50.12</td>
        <td>47.33</td>
        <td>37.25</td>
        <td>41.76</td>
        <td>33.14</td>
        <td>40.48</td>
        <td>46.01</td>
        <td>38.15</td>
        <td>37.81</td>
        <td>37.10</td>
        <td style="text-align: center;">39.43</td>
      </tr>
      <tr>
        <td style="text-align: center;">Flash-VStream</td>
        <td style="text-align: center;">VideoLLM</td>
        <td style="text-align: center;">7B</td>
        <td style="text-align: center;">8</td>
        <td>37.54</td>
        <td>44.74</td>
        <td>51.02</td>
        <td>47.95</td>
        <td>37.94</td>
        <td>42.72</td>
        <td>35.71</td>
        <td>44.24</td>
        <td>48.49</td>
        <td>38.95</td>
        <td>39.00</td>
        <td>38.80</td>
        <td style="text-align: center;">40.76</td>
      </tr>
      <tr style="background-color: #f9f9f9;">
        <td style="text-align: center;">InternVL2</td>
        <td style="text-align: center;">ImageLLM</td>
        <td style="text-align: center;">8B</td>
        <td style="text-align: center;">8</td>
        <td>40.53</td>
        <td>46.77</td>
        <td>52.38</td>
        <td>46.97</td>
        <td>40.35</td>
        <td>44.48</td>
        <td>38.92</td>
        <td>45.42</td>
        <td>50.45</td>
        <td>41.53</td>
        <td>42.35</td>
        <td>41.62</td>
        <td style="text-align: center;">43.05</td>
      </tr>
      <tr>
        <td style="text-align: center;">VILA</td>
        <td style="text-align: center;">ImageLLM</td>
        <td style="text-align: center;">8B</td>
        <td style="text-align: center;">8</td>
        <td>43.23</td>
        <td>49.30</td>
        <td>55.59</td>
        <td>52.47</td>
        <td>41.27</td>
        <td>47.07</td>
        <td>38.19</td>
        <td>44.27</td>
        <td>49.18</td>
        <td>41.29</td>
        <td>40.55</td>
        <td>40.38</td>
        <td style="text-align: center;">43.73</td>
      </tr>
      <tr style="background-color: #f9f9f9;">
        <td style="text-align: center;">VideoLLaMA2</td>
        <td style="text-align: center;">VideoLLM</td>
        <td style="text-align: center;">7B</td>
        <td style="text-align: center;">8</td>
        <td>42.50</td>
        <td>49.88</td>
        <td>55.96</td>
        <td>52.23</td>
        <td>41.40</td>
        <td>47.10</td>
        <td>38.95</td>
        <td>46.11</td>
        <td>51.77</td>
        <td>43.69</td>
        <td>42.22</td>
        <td>42.77</td>
        <td style="text-align: center;">44.94</td>
      </tr>
      <tr>
        <td style="text-align: center;">InternLM-XC2.5</td>
        <td style="text-align: center;">VideoLLM</td>
        <td style="text-align: center;">7B</td>
        <td style="text-align: center;">32</td>
        <td>46.51</td>
        <td>53.16</td>
        <td>59.84</td>
        <td>52.94</td>
        <td>45.87</td>
        <td>50.71</td>
        <td><strong>52.62</strong></td>
        <td><strong>58.55</strong></td>
        <td><strong>62.89</strong></td>
        <td><strong>53.98</strong></td>
        <td><strong>54.39</strong></td>
        <td><strong>54.39</strong></td>
        <td style="text-align: center;">52.55</td>
      </tr>
      <tr style="background-color: #f9f9f9;">
        <td style="text-align: center;">MiniCPM-V 2.6</td>
        <td style="text-align: center;">ImageLLM</td>
        <td style="text-align: center;">8B</td>
        <td style="text-align: center;">64</td>
        <td><strong>51.70</strong></td>
        <td><strong>59.50</strong></td>
        <td><strong>65.33</strong></td>
        <td><strong>61.72</strong></td>
        <td><strong>50.09</strong></td>
        <td><strong>56.63</strong></td>
        <td>46.44</td>
        <td>52.73</td>
        <td>58.35</td>
        <td><u>53.48</u></td>
        <td>48.32</td>
        <td>49.67</td>
        <td style="text-align: center;"><u>53.15</u></td>
      </tr>
      <tr>
        <td style="text-align: center;">Qwen2-VL</td>
        <td style="text-align: center;">ImageLLM</td>
        <td style="text-align: center;">7B</td>
        <td style="text-align: center;">8</td>
        <td><u>50.47</u></td>
        <td><u>57.71</u></td>
        <td><u>63.46</u></td>
        <td><u>60.77</u></td>
        <td><u>49.44</u></td>
        <td><u>55.29</u></td>
        <td><u>48.38</u></td>
        <td><u>55.17</u></td>
        <td><u>59.91</u></td>
        <td>52.04</td>
        <td><u>51.42</u></td>
        <td><u>51.39</u></td>
        <td style="text-align: center;"><strong>53.34</strong></td>
      </tr>
      <tr style="background-color: #e6e6e6;">
        <td colspan="17" style="text-align: center;"><strong>Closed-source LVLMs</strong></td>
      </tr>
      <tr>
        <td style="text-align: center;">Gemini 1.5 Pro</td>
        <td style="text-align: center;">-</td>
        <td style="text-align: center;">-</td>
        <td style="text-align: center;">1fps</td>
        <td>49.07</td>
        <td>56.15</td>
        <td>62.24</td>
        <td>58.36</td>
        <td>47.72</td>
        <td>53.68</td>
        <td>49.35</td>
        <td>55.77</td>
        <td>60.41</td>
        <td>52.89</td>
        <td>51.11</td>
        <td>51.55</td>
        <td style="text-align: center;">52.62</td>
      </tr>
      <tr style="background-color: #f9f9f9;">
        <td style="text-align: center;">GPT-4V</td>
        <td style="text-align: center;">-</td>
        <td style="text-align: center;">-</td>
        <td style="text-align: center;">10</td>
        <td>56.03</td>
        <td>62.61</td>
        <td>69.09</td>
        <td>65.36</td>
        <td>53.73</td>
        <td>60.30</td>
        <td>56.37</td>
        <td>61.41</td>
        <td>65.80</td>
        <td>59.18</td>
        <td>57.16</td>
        <td>57.93</td>
        <td style="text-align: center;">59.12</td>
      </tr>
      <tr>
        <td style="text-align: center;">GPT-4o</td>
        <td style="text-align: center;">-</td>
        <td style="text-align: center;">-</td>
        <td style="text-align: center;">25</td>
        <td><strong>58.26</strong></td>
        <td><strong>64.76</strong></td>
        <td><strong>70.75</strong></td>
        <td><strong>67.68</strong></td>
        <td><strong>55.82</strong></td>
        <td><strong>62.57</strong></td>
        <td><strong>57.99</strong></td>
        <td><strong>63.52</strong></td>
        <td><strong>67.72</strong></td>
        <td><strong>60.18</strong></td>
        <td><strong>59.25</strong></td>
        <td><strong>59.97</strong></td>
        <td style="text-align: center;"><strong>61.27</strong></td>
      </tr>
    </tbody>
  </table>
</div>

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
